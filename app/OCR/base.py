import cv2
import numpy as np
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def _preprocess(image_path: str) -> np.ndarray:
    img = cv2.imread(image_path)

    # Upscale small images — OCR struggles with small text
    h, w = img.shape[:2]
    if max(h, w) < 1500:
        scale = 1500 / max(h, w)
        img = cv2.resize(img, None, fx=scale, fy=scale, interpolation=cv2.INTER_CUBIC)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Denoise
    gray = cv2.fastNlMeansDenoising(gray, h=30)

    # Adaptive threshold works better than a fixed threshold on uneven lighting
    thresh = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 15
    )
    return thresh


def extract_text(image_path: str) -> str:
    """Run OCR on an image file and return the extracted raw text."""
    processed = _preprocess(image_path)
    config = "--oem 3 --psm 6"  # assume a uniform block of text
    return pytesseract.image_to_string(processed, config=config)