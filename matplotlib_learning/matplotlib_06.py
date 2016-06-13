import numpy as np
import matplotlib.pyplot as plt

"""
Contour Plot:
    It is a cross-section(横切面) of the three-dimensional graph of the function f(x, y) parallel to the x, y plane.
"""


def plot_01():
    xlist = np.linspace(-3.0, 3.0, 3)
    ylist = np.linspace(-3.0, 3.0, 4)
    X, Y = np.meshgrid(xlist, ylist)
    Z = np.sqrt(X ** 2 + Y ** 2)
    print(xlist, ylist)
    print(X)
    print(Y)
    print(Z)

    plt.figure()
    cp = plt.contour(X, Y, Z)
    plt.clabel(cp, inline=True, fontsize=10)
    plt.title('Contour Plot')
    plt.xlabel('x (cm)')
    plt.ylabel('y (cm)')
    plt.show()


def plot_02():
    xlist = np.linspace(-3.0, 3.0, 100)
    ylist = np.linspace(-3.0, 3.0, 100)
    X, Y = np.meshgrid(xlist, ylist)
    Z = np.sqrt(X ** 2 + Y ** 2)
    plt.figure()
    cp = plt.contourf(X, Y, Z)
    plt.colorbar(cp)
    plt.title('Filled Contours Plot')
    plt.xlabel('x (cm)')
    plt.ylabel('y (cm)')
    plt.show()


def plot_03():
    xlist = np.linspace(-3.0, 3.0, 100)
    ylist = np.linspace(-3.0, 3.0, 100)
    X, Y = np.meshgrid(xlist, ylist)
    Z = np.sqrt(X ** 2 + Y ** 2)
    plt.figure()
    levels = [0.0, 0.2, 0.5, 0.9, 1.5, 2.5, 3.5]
    contour = plt.contourf(X, Y, Z, levels)
    plt.clabel(contour, colors='k', fmt='%2.1f', fontsize=12)
    c = ('#ff0000', '#ffff00', '#0000FF', '0.6', 'c', 'm')
    contour_filled = plt.contourf(X, Y, Z, colors=c, levels=levels)
    plt.colorbar(contour_filled)
    plt.title('Filled Contours Plot')
    plt.xlabel('x (cm)')
    plt.ylabel('y (cm)')
    plt.show()


def plot_04():
    y, x = np.ogrid[-1:2:100j, -1:1:100j]
    plt.contour(x.ravel(),
                y.ravel(),
                x ** 2 + (y - ((x ** 2) ** (1.0 / 3))) ** 2,
                [1],
                colors='red', )
    plt.axis('equal')
    plt.show()


if __name__ == '__main__':
    plot_01()
    # plot_02()
    # plot_03()
    # plot_04()
