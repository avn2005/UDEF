from ocr.tesseract_engine import TesseractOCR

def get_ocr_engine(engine):
	if engine.lower() == "tesseract":
		return TesseractOCR()

	raise ValueError(f"Unsupported OCR engine: {engine}")

