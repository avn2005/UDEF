def get_ocr_engine(engine_name):
    engine_name = (engine_name or "tesseract").lower()

    if engine_name == "tesseract":
        from app.OCR.tesseract_engine import TesseractEngine

        return TesseractEngine()
    if engine_name == "easyocr":
        from app.OCR.easyocr_engine import EasyOCREngine

        return EasyOCREngine()
    if engine_name == "paddle":
        from app.OCR.paddle_engine import PaddleOCREngine

        return PaddleOCREngine()

    raise ValueError(f"Unsupported OCR engine: {engine_name}")
