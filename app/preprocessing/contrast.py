import cv2
import numpy as np


def histogram_equalization(img: np.ndarray) -> np.ndarray:
    """Apply global histogram equalization.

    Works for grayscale and color images. For color, converts to YCrCb and
    equalizes the Y channel.
    """
    if img is None:
        raise ValueError("Input image is None")

    # Grayscale
    if len(img.shape) == 2 or img.shape[2] == 1:
        return cv2.equalizeHist(img if img.dtype == np.uint8 else img.astype(np.uint8))

    # Color image: convert to YCrCb and equalize Y channel
    ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
    y, cr, cb = cv2.split(ycrcb)
    y_eq = cv2.equalizeHist(y)
    ycrcb_eq = cv2.merge([y_eq, cr, cb])
    return cv2.cvtColor(ycrcb_eq, cv2.COLOR_YCrCb2BGR)


def clahe(img: np.ndarray, clip_limit: float = 2.0, tile_grid_size: tuple = (8, 8)) -> np.ndarray:
    """Apply CLAHE (Contrast Limited Adaptive Histogram Equalization).

    Works for grayscale and color images. For color, applies CLAHE to the Y channel
    in YCrCb color space.
    """
    if img is None:
        raise ValueError("Input image is None")

    clahe_obj = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=tile_grid_size)

    if len(img.shape) == 2 or img.shape[2] == 1:
        img_u8 = img if img.dtype == np.uint8 else img.astype(np.uint8)
        return clahe_obj.apply(img_u8)

    ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
    y, cr, cb = cv2.split(ycrcb)
    y_clahe = clahe_obj.apply(y)
    ycrcb_clahe = cv2.merge([y_clahe, cr, cb])
    return cv2.cvtColor(ycrcb_clahe, cv2.COLOR_YCrCb2BGR)


def enhance_contrast(img: np.ndarray, method: str = 'clahe', **kwargs) -> np.ndarray:
    """Enhance contrast using specified method.

    method: 'clahe' | 'hist' | 'linear'
    For 'linear' you can pass alpha (gain) and beta (bias) as kwargs.
    """
    if method == 'clahe':
        return clahe(img, **kwargs)
    if method in ('hist', 'histeq', 'histogram'):
        return histogram_equalization(img)
    if method == 'linear':
        alpha = float(kwargs.get('alpha', 1.2))
        beta = float(kwargs.get('beta', 0))
        img_u8 = img if img.dtype == np.uint8 else img.astype(np.uint8)
        return cv2.convertScaleAbs(img_u8, alpha=alpha, beta=beta)
    raise ValueError(f"Unknown method: {method}")


if __name__ == '__main__':
    # quick manual test when run as script
    import sys

    if len(sys.argv) < 2:
        print('Usage: python contrast.py <image>')
        sys.exit(1)

    path = sys.argv[1]
    img = cv2.imread(path)
    out = enhance_contrast(img)
    cv2.imshow('enhanced', out)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
