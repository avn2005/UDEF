from app.OCR.easyocr_engine import EasyOCREngine
from app.OCR.paddle_engine import PaddleOCREngine
from app.OCR.tesseract_engine import TesseractEngine


def get_ocr_engine(engine_name):
    engine_name = (engine_name or "tesseract").lower()

    if engine_name == "tesseract":
        return TesseractEngine()
    if engine_name == "easyocr":
        return EasyOCREngine()
    if engine_name == "paddle":
        return PaddleOCREngine()

    raise ValueError(f"Unsupported OCR engine: {engine_name}")