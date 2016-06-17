import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy import misc
from img_utils import *


def process_image_01():
    img = misc.ascent()
    plt.gray()
    plt.axis('off')  # removes the axis and the ticks
    plt.imshow(img)
    print(img.dtype)
    print(img.shape)

    plt.show()


def process_image_02():
    img = misc.face()
    plt.gray()
    plt.axis('off')  # removes the axis and the ticks
    plt.imshow(img)
    print(img.dtype)
    print(img.shape)
    print(img.max)

    plt.show()


def process_image_03():
    img = mpimg.imread('bg.png')
    print(img.shape)
    plt.imshow(img)
    plt.axis('off')

    # lum_img = img[:, :, 1]
    # plt.imshow(lum_img)

    plt.show()


def process_image_04():
    charlie = mpimg.imread('charlie.png')
    #  colormaps plt.cm.datad
    cmaps = set(plt.cm.datad.keys())
    X = [(4, 3, 1, (1, 0, 0)), (4, 3, 2, (0.5, 0.5, 0)), (4, 3, 3, (0, 1, 0)),
         (4, 3, 4, (0, 0.5, 0.5)), (4, 3, (5, 8), (0, 0, 1)), (4, 3, 6, (1, 1, 0)),
         (4, 3, 7, (0.5, 1, 0)), (4, 3, 9, (0, 0.5, 0.5)),
         (4, 3, 10, (0, 0.5, 1)), (4, 3, 11, (0, 1, 1)), (4, 3, 12, (0.5, 1, 1))]
    fig = plt.figure(figsize=(12, 10))
    for nrows, ncols, plot_number, factor in X:
        sub = fig.add_subplot(nrows, ncols, plot_number)
        sub.set_xticks([])
        sub.set_yticks([])

        a, b, c = charlie[:, :, 0] * factor[0], charlie[:, :, 1] * factor[1], charlie[:, :, 2] * factor[2]
        charlie = np.dstack((a[:, :, np.newaxis], b[:, :, np.newaxis], c[:, :, np.newaxis]))
        sub.imshow(charlie, cmap=cmaps.pop())
    plt.show()


if __name__ == '__main__':
    process_image_01()
    # process_image_02()
    # process_image_03()
    # process_image_04()
