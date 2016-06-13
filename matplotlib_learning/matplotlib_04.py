import numpy as np
import matplotlib.pyplot as plt
from numpy import e, pi, sin, exp, cos
from matplotlib.gridspec import GridSpec

"""
Multiple Plots and Double Axes
"""


def plot_01():
    python_course_green = "#476042"
    plt.figure(figsize=(6, 4))
    plt.subplot(221)  # equivalent to: plt.subplot(2, 2, 1)
    plt.text(0.5,  # x coordinate, 0 leftmost positioned, 1 rightmost
             0.5,  # y coordinate, 0 bottommost positioned, 1 topmost
             'subplot(2,2,1)',  # the text which will be printed
             horizontalalignment='center',  # shortcut 'ha'
             verticalalignment='center',  # shortcut 'va'
             fontsize=20, alpha=.5
             )
    plt.subplot(224, axisbg=python_course_green)
    # get rid of the ticks on the axes
    plt.xticks(())
    plt.yticks(())
    plt.text(0.5, 0.5,
             'subplot(2,2,4)',
             ha='center', va='center',
             fontsize=20, color="y")
    plt.show()


def plot_02():
    def f(t):
        return exp(-t) * cos(2 * pi * t)

    def fp(t):
        return -2 * pi * exp(-t) * sin(2 * pi * t) - e ** (-t) * cos(2 * pi * t)

    def g(t):
        return sin(t) * cos(1 / t)

    fig = plt.figure(figsize=(6, 4))
    t = np.arange(-5.0, 1.0, 0.1)
    sub1 = fig.add_subplot(221)  # instead of plt.subplot(2, 2, 1)
    sub1.set_title('The function f')  # non OOP: plt.title('The function f')
    sub1.plot(t, f(t))
    sub2 = fig.add_subplot(222, axisbg="lightgrey")
    sub2.set_title('fp, the derivation of f')
    sub2.plot(t, fp(t))
    t = np.arange(-3.0, 2.0, 0.02)
    sub3 = fig.add_subplot(223)
    sub3.set_title('The function g')
    sub3.plot(t, g(t))
    t = np.arange(-0.2, 0.2, 0.001)
    sub4 = fig.add_subplot(224, axisbg="lightgrey")
    sub4.set_title('A closer look at g')
    sub4.set_xticks([-0.2, -0.1, 0, 0.1, 0.2])
    sub4.set_yticks([-0.15, -0.1, 0, 0.1, 0.15])
    sub4.plot(t, g(t), '-g')
    plt.tight_layout()
    plt.show()


def plot_03():
    X = [(2, 1, 1), (2, 3, 4), (2, 3, 5), (2, 3, 6)]
    fig = plt.figure(figsize=(6, 4))
    fig.subplots_adjust(bottom=0.025, left=0.025, top=0.975, right=0.975)
    for nrows, ncols, plot_number in X:
        plt.subplot(nrows, ncols, plot_number)
        plt.xticks(())
        plt.yticks(())
    plt.show()


def plot_04():
    fig = plt.figure()
    gs = GridSpec(1, 1,
                  bottom=0.2,
                  left=0.15,
                  top=0.8)
    fig.add_subplot(gs[0, 0])
    plt.show()


def plot_05():
    plt.figure(figsize=(6, 4))
    G = GridSpec(3, 3)
    X = np.linspace(0, 2 * np.pi, 50, endpoint=True)
    F1 = 2.8 * np.cos(X)
    F2 = 5 * np.sin(X)
    F3 = 0.3 * np.sin(X)
    axes_1 = plt.subplot(G[0, :])
    axes_1.plot(X, F1, 'r-', X, F2)
    axes_2 = plt.subplot(G[1, :-1])
    axes_2.plot(X, F3)
    axes_3 = plt.subplot(G[1:, -1])
    axes_3.plot([1, 2, 3, 4], [1, 10, 100, 1000], 'b-')
    axes_4 = plt.subplot(G[-1, 0])
    axes_4.plot([1, 2, 3, 4], [47, 11, 42, 60], 'r-')
    axes_5 = plt.subplot(G[-1, -2])
    axes_5.plot([1, 2, 3, 4], [7, 5, 4, 3.8])
    plt.tight_layout()
    plt.show()


def plot_06():
    """ Logarithmic Scale """
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    x = np.arange(0, 5, 0.25)
    ax.plot(x, x ** 2, x, x ** 3)
    ax.set_yscale("log")
    ax.axis('tight')
    # Plot Grid
    plt.grid(color='b', alpha=0.5, linestyle='dashed', linewidth=0.5)
    plt.show()


if __name__ == '__main__':
    plot_01()
    # plot_02()
    # plot_03()
    # plot_04()
    # plot_05()
    # plot_06()
