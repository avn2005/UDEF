
from ocr.factory import get_ocr_engine


def extract_text(image, engine="tesseract"):
	"""Extract text from an image using the specified OCR engine.

	Args:
		image: Image path or image object accepted by the OCR engine.
		engine: Name of the OCR engine to use (default: "tesseract").

	Returns:
		Extracted text as a string.
	"""
	ocr = get_ocr_engine(engine)
	return ocr.extract_text(image)

