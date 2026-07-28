class PaddleOCREngine:
    def __init__(self):
        self.ocr = None
        try:
            from paddleocr import PaddleOCR
        except ImportError:
            return

        self.ocr = PaddleOCR(
            use_angle_cls=True,
            lang="en"
        )

    def extract_text(self, image):
        """
        Extract text from an image using PaddleOCR.

        Args:
            image: Path to image

        Returns:
            Extracted text as a string
        """
        if self.ocr is None:
            return ""

        try:
            result = self.ocr.ocr(image, cls=True)
        except Exception:
            return ""

        extracted_text = []

        if result:
            for line in result:
                if line:
                    for word in line:
                        extracted_text.append(word[1][0])

        return "\n".join(extracted_text)