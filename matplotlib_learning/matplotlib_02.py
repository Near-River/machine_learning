import numpy as np
import matplotlib.pyplot as plt


def plot_01():
    X = np.linspace(0, 2 * np.pi, 50, endpoint=True)
    F = np.sin(X)
    plt.plot(X, F)
    startx, endx = -0.1, 2 * np.pi + 0.1
    starty, endy = -1.1, 1.1
    plt.axis([startx, endx, starty, endy])
    plt.show()


def plot_02():
    X = np.linspace(-2 * np.pi, 2 * np.pi, 50, endpoint=True)
    F1 = 3 * np.sin(X)
    F2 = np.sin(2 * X)
    F3 = 0.3 * np.sin(X)
    startx, endx = -2 * np.pi - 0.1, 2 * np.pi + 0.1
    starty, endy = -3.1, 3.1
    plt.axis([startx, endx, starty, endy])
    plt.plot(X, F1)
    plt.plot(X, F2)
    plt.plot(X, F3)
    plt.plot(X, F1, 'ro')
    plt.plot(X, F2, 'bx')
    plt.show()


def plot_03():
    n = 256
    X = np.linspace(-np.pi, np.pi, n, endpoint=True)
    Y = np.sin(2 * X)
    plt.plot(X, Y, color='blue', alpha=1.00)
    plt.plot(X, 0 * X)
    plt.fill_between(X, 0, Y, color='blue', alpha=.1)
    plt.show()


if __name__ == '__main__':
    plot_01()
    # plot_02()
    # plot_03()
