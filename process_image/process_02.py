import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from img_utils import imag_tile, shade
from PIL import Image

basic_img = mpimg.imread('bg.png')
decorators_img = imag_tile(basic_img, 3, 3)


def process_image_01():
    plt.axis('off')
    print(decorators_img.shape)

    """crop image"""
    # cropped = basic_img[50:90, 80:120]
    # plt.imshow(cropped)

    plt.imshow(decorators_img)
    plt.show()


def process_image_02():
    """blend images"""
    global decorators_img

    at_img = mpimg.imread('at_sign.png')
    # at_img and decorators_img have to be of equal size:
    d_shape = decorators_img.shape
    at_shape = at_img.shape
    height, width, colours = [min(x) for x in zip(*(d_shape, at_shape))]

    at_img = at_img[0:height, 0:width]
    decorators_img = decorators_img[0:height, 0:width]
    print(at_img.shape, decorators_img.shape)
    tinted_decorator_img = shade(decorators_img, 0.5)

    blend_img = np.where(at_img > [0.1, 0.1, 0.1], decorators_img, tinted_decorator_img)
    plt.imshow(blend_img)
    plt.show()


def process_image_03():
    # PIL: pixel are within range 0 and 255
    # mpimg: range 0 bis 1
    img = Image.open('bg.png')
    img = np.asarray(img, np.float)
    img /= 255
    print(img.shape)

    plt.axis('off')
    plt.imshow(img)
    plt.show()


if __name__ == '__main__':
    # process_image_01()
    # process_image_02()
    process_image_03()
