def rotate90(matrix):
    """Rotate a 2D sequence clockwise by 90 degrees."""
    if not matrix:
        return matrix
    return [list(reversed(col)) for col in zip(*matrix)]


def rotate180(matrix):
    """Rotate a 2D sequence by 180 degrees."""
    if not matrix:
        return matrix
    return [list(reversed(row)) for row in reversed(matrix)]


def rotate270(matrix):
    """Rotate a 2D sequence clockwise by 270 degrees."""
    if not matrix:
        return matrix
    return [list(col) for col in zip(*reversed(matrix))]


def auto_rotate(matrix, orientation=None):
    """Rotate a 2D sequence using an orientation angle.

    Supported orientation values are 90, 180, 270. If orientation is None
    or an unsupported value is provided, the original matrix is returned.
    """
    if orientation is None:
        return matrix
    angle = orientation % 360
    if angle == 90:
        return rotate90(matrix)
    if angle == 180:
        return rotate180(matrix)
    if angle == 270:
        return rotate270(matrix)
    return matrix
