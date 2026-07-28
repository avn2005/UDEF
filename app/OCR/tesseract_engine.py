try:
    import pytesseract
except ImportError:  # pragma: no cover - optional dependency
    pytesseract = None


class TesseractEngine:
    """Simple wrapper around pytesseract for extracting text."""

    def extract_text(self, image):
        """Extract text from an image path or PIL Image."""
        if pytesseract is None:
            return ""

        try:
            return pytesseract.image_to_string(image).strip()
        except Exception:
            return ""