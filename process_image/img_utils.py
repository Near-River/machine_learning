import numpy as np
import matplotlib.image as mpimg


def tint(imag, percent):
    """
    imag: the image which will be whitened
    percent: a value between 0 (image will remain unchanged)
             and 1 (image will completely white)
    """
    tinted_imag = imag + (np.ones(imag.shape) - imag) * percent
    return tinted_imag


def shade(imag, percent):
    """
    imag: the image which will be shaded
    percent: a value between 0 (image will remain unchanged
             and 1 (image will be blackened)
    """
    shaded_imag = imag * (1 - percent)
    return shaded_imag


def vertical_gradient_line(image, reverse=False):
    """
    We create a horizontal gradient line with the shape (1, image.shape[1], 3))
    The values are incremented from 0 to 1, if reverse is False,
    otherwise the values are decremented from 1 to 0.
    """
    number_of_columns = image.shape[1]
    if reverse:
        C = np.linspace(1, 0, number_of_columns)
    else:
        C = np.linspace(0, 1, number_of_columns)
    count = image.shape[2]
    res = [C for i in range(count)]
    C = np.dstack(tuple(res))
    return C


def horizontal_gradient_line(image, reverse=False):
    """
    We create a vertical gradient line with the shape (image.shape[0], 1, 3))
    The values are incremented from 0 to 1, if reverse is False,
    otherwise the values are decremented from 1 to 0.
    """
    number_of_rows, number_of_columns = image.shape[:2]
    if reverse:
        C = np.linspace(1, 0, number_of_rows)
    else:
        C = np.linspace(0, 1, number_of_rows)
    C = C[np.newaxis, :]
    C = np.concatenate((C, C, C)).transpose()
    C = C[:, np.newaxis]
    return C


def imag_tile(img, n, m=1):
    """
    The image 'img' will be repeated ntimes in vertical and
    m times in horizontal direction.
    """
    if n == 1:
        tiled_img = img
    else:
        lst_imags = []
        for i in range(n):
            lst_imags.append(img)
            tiled_img = np.concatenate(lst_imags, axis=1)
    if m > 1:
        lst_imags = []
        for i in range(m):
            lst_imags.append(tiled_img)
        tiled_img = np.concatenate(lst_imags, axis=0)

    return tiled_img
