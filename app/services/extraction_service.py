import io
from pathlib import Path

from PIL import Image, UnidentifiedImageError

from app.OCR.extractor import extract_text
from llm.extractor import extract_data


class ExtractionService:
    @staticmethod
    def extract(file_content: bytes, document_type: str | None = None):
        """Extract text from uploaded image content and return structured extracted data."""
        try:
            image = Image.open(io.BytesIO(file_content))
            image.load()
        except (UnidentifiedImageError, OSError, ValueError):
            return {"ocr_text": "", "error": "Uploaded content is not a valid image"}

        temp_path = Path("temp_upload.png")
        image.save(temp_path)
        text = extract_text(str(temp_path), engine="tesseract")
        extracted = extract_data(text, document_type or "generic")

        return {
            "ocr_text": text,
            "extracted_data": extracted,
        }