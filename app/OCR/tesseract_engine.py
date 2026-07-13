import pytesseract


class TesseractOCR:
	"""Simple wrapper around pytesseract for extracting text from images."""

	def extract_text(self, image) -> str:
		"""Return extracted text from a PIL Image or image file path."""
		return pytesseract.image_to_string(image)


