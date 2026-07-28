from app.OCR.factory import get_ocr_engine


def extract_text(image, engine="tesseract"):
    """Extract text from an image using the specified OCR engine."""
    try:
        ocr = get_ocr_engine(engine)
        return ocr.extract_text(image) or ""
    except Exception:
        return ""

