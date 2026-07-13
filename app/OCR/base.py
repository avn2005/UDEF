import io

from PIL import Image
import pytesseract
import numpy as np
import cv2


def extract_text(image):
    """Extract text from an image.

    Args:
        image: A path to an image file, bytes, PIL Image, or OpenCV image array.

    Returns:
        str: Extracted text from the image.
    """
    if isinstance(image, str):
        img = Image.open(image)
    elif isinstance(image, bytes):
        img = Image.open(io.BytesIO(image))
    elif isinstance(image, np.ndarray):
        # Convert BGR OpenCV image to RGB PIL Image.
        img = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    else:
        img = image

    return pytesseract.image_to_string(img).strip()
