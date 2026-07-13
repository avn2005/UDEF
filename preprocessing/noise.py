import cv2
import numpy as np
from typing import Optional


def gaussian_filter(image: np.ndarray, ksize: int = 5, sigma: float = 0) -> np.ndarray:
    """Apply Gaussian blur to an image.

    Args:
        image: Input image (grayscale or color).
        ksize: Kernel size (must be odd).
        sigma: Standard deviation in X and Y direction. 0 means calculated from ksize.

    Returns:
        Blurred image as numpy.ndarray.
    """
    if ksize % 2 == 0:
        ksize += 1
    return cv2.GaussianBlur(image, (ksize, ksize), sigma)


def median_filter(image: np.ndarray, ksize: int = 5) -> np.ndarray:
    """Apply median filter to an image.

    Args:
        image: Input image (grayscale or color).
        ksize: Aperture linear size; must be odd and greater than 1.

    Returns:
        Filtered image as numpy.ndarray.
    """
    if ksize % 2 == 0:
        ksize += 1
    return cv2.medianBlur(image, ksize)


def bilateral_filter(image: np.ndarray, diameter: int = 9, sigma_color: float = 75, sigma_space: float = 75) -> np.ndarray:
    """Apply bilateral filter to an image.

    Args:
        image: Input image (grayscale or color).
        diameter: Diameter of each pixel neighborhood.
        sigma_color: Filter sigma in the color space.
        sigma_space: Filter sigma in the coordinate space.

    Returns:
        Filtered image as numpy.ndarray.
    """
    return cv2.bilateralFilter(image, diameter, sigma_color, sigma_space)


def remove_noise(image: np.ndarray, method: str = "gaussian", **kwargs) -> np.ndarray:
    """Remove noise from an image using a chosen method.

    Supported methods: 'gaussian', 'median', 'bilateral'.

    Args:
        image: Input image.
        method: One of 'gaussian', 'median', 'bilateral'.
        **kwargs: Parameters forwarded to the chosen filter function.

    Returns:
        Denoised image.
    """
    method = method.lower()
    if method == "gaussian":
        return gaussian_filter(image, **kwargs)
    if method == "median":
        return median_filter(image, **kwargs)
    if method == "bilateral":
        return bilateral_filter(image, **kwargs)
    raise ValueError(f"Unsupported method '{method}'. Choose 'gaussian', 'median', or 'bilateral'.")


if __name__ == "__main__":
    # simple demo when run directly
    import sys

    if len(sys.argv) > 1:
        img = cv2.imread(sys.argv[1])
        out = remove_noise(img, method="bilateral")
        cv2.imwrite("denoised.png", out)
