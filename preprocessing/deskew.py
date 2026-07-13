import cv2
import numpy as np

def calculate_skew(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    coords = np.column_stack(np.where(gray > 0))

    angle = cv2.minAreaRect(coords)[-1]

    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle

    return angle


def deskew_image(image):
    angle = calculate_skew(image)

    (h, w) = image.shape[:2]

    center = (w // 2, h // 2)

    matrix = cv2.getRotationMatrix2D(center, angle, 1.0)

    rotated = cv2.warpAffine(
        image,
        matrix,
        (w, h),
        flags=cv2.INTER_CUBIC,
        borderMode=cv2.BORDER_REPLICATE,
    )

    return rotated
