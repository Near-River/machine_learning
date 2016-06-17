import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


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


if __name__ == '__main__':
    basic_img = mpimg.imread('charlie.png')
    decorators_img = imag_tile(basic_img, 3, 3)
    plt.axis('off')
    print(decorators_img.shape)

    """crop image"""
    # cropped = basic_img[50:90, 80:120]
    # plt.imshow(cropped)

    plt.imshow(decorators_img)
    plt.show()
