import cv2


def binary_threshold(image, thresh=127, maxval=255, threshold_type=cv2.THRESH_BINARY):
    """Apply a fixed-level binary threshold to an image.

    Args:
        image: Input grayscale image.
        thresh: Threshold value.
        maxval: Maximum value to use with the THRESH_BINARY thresholding.
        threshold_type: OpenCV threshold type.

    Returns:
        thresholded image.
    """
    _, result = cv2.threshold(image, thresh, maxval, threshold_type)
    return result


def otsu_threshold(image, maxval=255):
    """Apply Otsu's thresholding to an image.

    Args:
        image: Input grayscale image.
        maxval: Maximum value to use with the thresholding.

    Returns:
        thresholded image.
    """
    _, result = cv2.threshold(image, 0, maxval, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return result


def adaptive_mean(image, maxval=255, block_size=11, C=2):
    """Apply adaptive mean thresholding to an image.

    Args:
        image: Input grayscale image.
        maxval: Maximum value to use with the thresholding.
        block_size: Size of a pixel neighborhood used to calculate the threshold.
        C: Constant subtracted from the mean.

    Returns:
        thresholded image.
    """
    result = cv2.adaptiveThreshold(
        image,
        maxval,
        cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY,
        block_size,
        C,
    )
    return result


def adaptive_gaussian(image, maxval=255, block_size=11, C=2):
    """Apply adaptive Gaussian thresholding to an image.

    Args:
        image: Input grayscale image.
        maxval: Maximum value to use with the thresholding.
        block_size: Size of a pixel neighborhood used to calculate the threshold.
        C: Constant subtracted from the weighted sum.

    Returns:
        thresholded image.
    """
    result = cv2.adaptiveThreshold(
        image,
        maxval,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        block_size,
        C,
    )
    return result
