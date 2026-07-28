from paddleocr import PaddleOCR

class PaddleOCREngine:
    def __init__(self):
        # Initialize PaddleOCR only once
        self.ocr = PaddleOCR(
            use_angle_cls=True,
            lang="en"
        )

    def extract_text(self, image):
        """
        Extract text from an image using PaddleOCR.

        Args:
            image: Image path

        Returns:
            Extracted text as a single string.
        """
        result = self.ocr.ocr(image, cls=True)

        text = []

        if result:
            for line in result:
                if line:
                    for word in line:
                        text.append(word[1][0])

        return "\n".join(text)