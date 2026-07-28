import importlib
import sys


def test_ocr_extractor_imports_without_optional_ocr_dependencies():
    sys.modules.pop("app.OCR.extractor", None)
    module = importlib.import_module("app.OCR.extractor")

    assert hasattr(module, "extract_text")
    assert callable(module.extract_text)
