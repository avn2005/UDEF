import re
from typing import Any, Dict


def _find_pattern(text: str, patterns: list[str]) -> str | None:
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return match.group(1).strip()
    return None


def _find_pan(text: str) -> str | None:
    match = re.search(r"\b([A-Z]{5}[0-9]{4}[A-Z])\b", text)
    return match.group(1) if match else None


def _find_aadhaar(text: str) -> str | None:
    match = re.search(r"\b(\d{4})[\s-]?(\d{4})[\s-]?(\d{4})\b", text)
    if not match:
        return None
    return "".join(match.groups())


def _clean_line(line: str) -> str:
    """Strip leading/trailing non-letter noise, collapse extra spaces."""
    line = re.sub(r"^[^A-Za-z]+", "", line)
    line = re.sub(r"[^A-Za-z]+$", "", line)
    return re.sub(r"\s+", " ", line).strip()


def _extract_letter_words(line: str) -> str:
    """Pull out only alphabetic word tokens (2+ letters) from a noisy line."""
    words = re.findall(r"[A-Za-z]{2,}", line)
    return " ".join(words)


_NAME_SKIP_WORDS = {
    "GOVERNMENT", "INDIA", "GOVT", "OFINDIA", "INCOMETAX", "INCOME", "TAX",
    "DEPARTMENT", "PERMANENT", "ACCOUNT", "NUMBER", "SIGNATURE", "UNIQUE",
    "IDENTIFICATION", "AUTHORITY", "AADHAAR", "ENROLMENT", "VID", "MALE",
    "FEMALE", "DOB", "DATE", "BIRTH", "ADDRESS", "REPUBLIC",
}


def _find_name(text: str) -> str | None:
    name = _find_pattern(text, [r"name[:\s]*(.+)", r"full\s*name[:\s]*(.+)"])
    if name:
        cleaned = _clean_line(name)
        if cleaned:
            return cleaned

    lines = [line.strip() for line in text.splitlines() if line.strip()]
    for line in lines[:8]:
        cleaned = _clean_line(line)

        if re.match(r"^[A-Z][A-Z\s&\-]+$", cleaned) and len(cleaned.split()) >= 2:
            return cleaned
        if re.match(r"^[A-Z][a-z]+(?:\s+[A-Z][a-z]+)+$", cleaned):
            return cleaned

        # Fallback: extract clean letter-only words from noisy lines
        letters_only = _extract_letter_words(line)
        words = letters_only.split()
        if len(words) >= 2 and all(w[0].isupper() or w.isupper() for w in words):
            if not any(w.upper() in _NAME_SKIP_WORDS for w in words):
                return letters_only

    return None


def _normalize_document_type(document_type: str) -> str:
    normalized = (document_type or "").strip().lower()
    normalized = normalized.replace("-", " ").replace("_", " ")
    normalized = " ".join(normalized.split())
    aliases = {
        "id card": "id_card",
        "identity card": "id_card",
        "idcard": "id_card",
        "aadhar": "aadhaar_card",
        "aadhaar": "aadhaar_card",
        "aadhar card": "aadhaar_card",
        "aadhaar card": "aadhaar_card",
        "pan": "pan_card",
        "pan card": "pan_card",
        "invoice": "invoice",
        "inv": "invoice",
        "receipt": "receipt",
        "passport": "passport",
        "driving license": "driving_license",
        "driving licence": "driving_license",
        "dl": "driving_license",
        "auto": "auto",
    }
    return aliases.get(normalized, normalized.replace(" ", "_"))


def _detect_document_type(text: str) -> str:
    """Guess document type from OCR text patterns when document_type is 'auto'."""
    if re.search(r"pan\s*card|income\s*tax\s*department", text, re.I) or (
        _find_pan(text) and not re.search(r"aadhaar|passport|licen[cs]e", text, re.I)
    ):
        return "pan_card"
    if re.search(r"aadhaar|uidai|unique\s*identification", text, re.I) or _find_aadhaar(text):
        return "aadhaar_card"
    if re.search(r"passport", text, re.I):
        return "passport"
    if re.search(r"driving\s*licen[cs]e|transport\s*department|dl\s*no", text, re.I):
        return "driving_license"
    return "generic"


def extract_data(ocr_text: str, document_type: str) -> Dict[str, Any]:
    """Extract structured fields from OCR text based on document type."""
    text = ocr_text or ""
    doc_type = _normalize_document_type(document_type)

    if doc_type == "auto":
        doc_type = _detect_document_type(text)

    result: Dict[str, Any] = {
        "document_type": doc_type,
        "name": _find_name(text),
        "pan": _find_pan(text),
        "aadhaar": _find_aadhaar(text),
        "date_of_birth": _find_pattern(text, [r"\b([0-9]{2}[/-][0-9]{2}[/-][0-9]{4})\b"]),
        "raw_text": text,
    }

    if doc_type == "invoice":
        result.update(
            {
                "invoice_number": _find_pattern(text, [r"invoice\s*(?:no\.?|#)[:\s]*([A-Z0-9-]+)", r"(?:invoice|inv)\s*[:\s]*([A-Z0-9-]+)"]),
                "invoice_date": _find_pattern(text, [r"(?:invoice\s*date|date)[:\s]*([0-9]{1,2}[/-][0-9]{1,2}[/-][0-9]{2,4})"]),
                "total_amount": _find_pattern(text, [r"(?:total\s*due|amount\s*due|total)[:\s]*\$?\s*([0-9,]+\.?[0-9]{0,2})"]),
                "vendor": _find_pattern(text, [r"(?:vendor|from|supplier)[:\s]*(.+)", r"bill\s*from[:\s]*(.+)"]),
            }
        )
    elif doc_type == "receipt":
        result.update(
            {
                "store_name": _find_pattern(text, [r"^([A-Z][A-Z\s&\-]+)$", r"store[:\s]*(.+)"]),
                "receipt_date": _find_pattern(text, [r"(?:date)[:\s]*([0-9]{1,2}[/-][0-9]{1,2}[/-][0-9]{2,4})"]),
                "total_paid": _find_pattern(text, [r"(?:total\s*paid|amount\s*paid|total)[:\s]*\$?\s*([0-9,]+\.?[0-9]{0,2})"]),
                "tax": _find_pattern(text, [r"(?:tax|sales\s*tax)[:\s]*\$?\s*([0-9,]+\.?[0-9]{0,2})"]),
            }
        )
    elif doc_type == "passport":
        result.update(
            {
                "passport_number": _find_pattern(text, [r"passport\s*no\.?[:\s]*([A-Z0-9]+)", r"passport\s*number[:\s]*([A-Z0-9]+)"]),
                "surname": _find_pattern(text, [r"surname[:\s]*(.+)", r"last\s*name[:\s]*(.+)"]),
                "given_names": _find_pattern(text, [r"given\s*names?[:\s]*(.+)", r"first\s*name[:\s]*(.+)"]),
                "nationality": _find_pattern(text, [r"nationality[:\s]*(.+)"]),
                "expiry_date": _find_pattern(text, [r"date\s*of\s*expiry[:\s]*([0-9]{1,2}[/-][0-9]{1,2}[/-][0-9]{2,4})", r"expiry[:\s]*([0-9]{1,2}[/-][0-9]{1,2}[/-][0-9]{2,4})"]),
            }
        )
    elif doc_type == "id_card":
        result.update(
            {
                "id_number": _find_pattern(text, [r"id\s*no\.?[:\s]*([A-Z0-9]+)", r"id\s*number[:\s]*([A-Z0-9]+)"]),
                "address": _find_pattern(text, [r"address[:\s]*(.+)"]),
            }
        )
    elif doc_type == "pan_card":
        result.update(
            {
                "pan": _find_pan(text),
                "name": _find_name(text),
            }
        )
    elif doc_type == "aadhaar_card":
        result.update(
            {
                "aadhaar": _find_aadhaar(text),
                "name": _find_name(text),
                "address": _find_pattern(text, [r"address[:\s]*(.+)"]),
            }
        )
    elif doc_type == "driving_license":
        result.update(
            {
                "license_number": _find_pattern(text, [r"dl\s*no\.?[:\s]*([A-Z0-9-]+)", r"licen[cs]e\s*no\.?[:\s]*([A-Z0-9-]+)"]),
                "valid_till": _find_pattern(text, [r"valid\s*till[:\s]*([0-9]{1,2}[/-][0-9]{1,2}[/-][0-9]{2,4})"]),
            }
        )
    else:
        result["message"] = "Unsupported document type. Returning raw OCR text plus identity fields."

    return result