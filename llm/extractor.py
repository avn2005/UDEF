import re
from typing import Any, Dict


def _find_pattern(text: str, patterns: list[str]) -> str | None:
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return match.group(1).strip()
    return None


def _normalize_document_type(document_type: str) -> str:
    normalized = (document_type or "").strip().lower()
    normalized = normalized.replace("-", " ").replace("_", " ")
    normalized = " ".join(normalized.split())
    aliases = {
        "id card": "id_card",
        "identity card": "id_card",
        "idcard": "id_card",
        "invoice": "invoice",
        "inv": "invoice",
        "receipt": "receipt",
        "passport": "passport",
    }
    return aliases.get(normalized, normalized.replace(" ", "_"))


def extract_data(ocr_text: str, document_type: str) -> Dict[str, Any]:
    """Extract structured fields from OCR text based on document type."""
    text = ocr_text or ""
    doc_type = _normalize_document_type(document_type)
    result: Dict[str, Any] = {"document_type": doc_type, "raw_text": text}

    if doc_type == "invoice":
        result.update(
            {
                "invoice_number": _find_pattern(text, [r"invoice\s*(?:no\.?|#)[:\s]*([A-Z0-9-]+)", r"(?:invoice|inv)\s*[:\s]*([A-Z0-9-]+)"]),
                "invoice_date": _find_pattern(text, [r"(?:invoice\s*date|date)[:\s]*([0-9]{1,2}[/-][0-9]{1,2}[/-][0-9]{2,4})"]),
                "total_amount": _find_pattern(text, [r"(?:total\s*due|amount\s*due|total)[:\s]*\$?\s*([0-9,]+\.?[0-9]{0,2})"]),
                "vendor": _find_pattern(text, [r"(?:vendor|from|supplier)[:\s]*(.+)", r"bill\s*from[:\s]*(.+)"])
            }
        )
    elif doc_type == "receipt":
        result.update(
            {
                "store_name": _find_pattern(text, [r"^([A-Z][A-Z\s&\-]+)$", r"store[:\s]*(.+)"]),
                "receipt_date": _find_pattern(text, [r"(?:date)[:\s]*([0-9]{1,2}[/-][0-9]{1,2}[/-][0-9]{2,4})"]),
                "total_paid": _find_pattern(text, [r"(?:total\s*paid|amount\s*paid|total)[:\s]*\$?\s*([0-9,]+\.?[0-9]{0,2})"]),
                "tax": _find_pattern(text, [r"(?:tax|sales\s*tax)[:\s]*\$?\s*([0-9,]+\.?[0-9]{0,2})"])
            }
        )
    elif doc_type == "passport":
        result.update(
            {
                "passport_number": _find_pattern(text, [r"passport\s*no\.?[:\s]*([A-Z0-9]+)", r"passport\s*number[:\s]*([A-Z0-9]+)"]),
                "surname": _find_pattern(text, [r"surname[:\s]*(.+)", r"last\s*name[:\s]*(.+)"]),
                "given_names": _find_pattern(text, [r"given\s*names?[:\s]*(.+)", r"first\s*name[:\s]*(.+)"]),
                "nationality": _find_pattern(text, [r"nationality[:\s]*(.+)"]),
                "date_of_birth": _find_pattern(text, [r"date\s*of\s*birth[:\s]*([0-9]{1,2}[/-][0-9]{1,2}[/-][0-9]{2,4})"]),
                "expiry_date": _find_pattern(text, [r"date\s*of\s*expiry[:\s]*([0-9]{1,2}[/-][0-9]{1,2}[/-][0-9]{2,4})", r"expiry[:\s]*([0-9]{1,2}[/-][0-9]{1,2}[/-][0-9]{2,4})"])
            }
        )
    elif doc_type == "id_card":
        result.update(
            {
                "id_number": _find_pattern(text, [r"id\s*no\.?[:\s]*([A-Z0-9]+)", r"id\s*number[:\s]*([A-Z0-9]+)"]),
                "name": _find_pattern(text, [r"name[:\s]*(.+)", r"full\s*name[:\s]*(.+)"]),
                "date_of_birth": _find_pattern(text, [r"date\s*of\s*birth[:\s]*([0-9]{1,2}[/-][0-9]{1,2}[/-][0-9]{2,4})"]),
                "address": _find_pattern(text, [r"address[:\s]*(.+)"])
            }
        )
    else:
        result["message"] = "Unsupported document type. Returning raw OCR text."

    return result
