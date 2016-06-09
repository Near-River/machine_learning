import numpy as np
import matplotlib.pyplot as plt

"""
Spines and Ticks
"""


def plot_01():
    X = np.linspace(-2 * np.pi, 2 * np.pi, 70, endpoint=True)
    F1 = np.sin(2 * X)
    F2 = (2 * X ** 5 + 4 * X ** 4 - 4.8 * X ** 3 + 1.2 * X ** 2 + X + 1) * np.exp(-X ** 2)
    # get the current axes, creating them if necessary:
    ax = plt.gca()
    # making the top and right spine invisible:
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    # making the bottom and left spine red color:
    ax.spines['bottom'].set_color('red')
    ax.spines['left'].set_color('red')
    # moving bottom spine up to y=0 position:
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data', 0))
    # moving left spine to the right to position x == 0:
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data', 0))
    plt.plot(X, F1)
    plt.plot(X, F2)
    plt.show()


def plot_02():
    X = np.linspace(-2 * np.pi, 2 * np.pi, 70, endpoint=True)
    F1 = np.sin(X ** 2)
    F2 = X * np.sin(X)
    ax = plt.gca()
    # moving bottom spine up to y=0 position:
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data', 0))
    # moving left spine to the right to position x == 0:
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data', 0))
    plt.xticks([-6.28, -3.14, 3.14, 6.28],
               [r'$-2\pi$', r'$-\pi$', r'$+\pi$', r'$+2\pi$'])
    plt.yticks([-3, -1, 0, +1, 3])

    plt.plot(X, F1)
    plt.plot(X, F2)
    plt.show()

    for xtick_label in ax.get_xticklabels():
        print(xtick_label)
    labels = [xtick_label.get_text() for xtick_label in ax.get_xticklabels()]
    print(labels)


def plot_03():
    X = np.linspace(-2 * np.pi, 2 * np.pi, 70, endpoint=True)
    F1 = np.sin(X)
    ax = plt.gca()
    # moving bottom spine up to y=0 position:
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data', 0))
    # moving left spine to the right to position x == 0:
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data', 0))
    plt.xticks([-6.28, -3.14, 3.14, 6.28],
               [r'$-2\pi$', r'$-\pi$', r'$+\pi$', r'$+2\pi$'])
    plt.yticks([-3, -1, 0, +1, 3])

    for xtick in ax.get_xticklabels():
        xtick.set_fontsize(18)
        xtick.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.7))
    for ytick in ax.get_yticklabels():
        ytick.set_fontsize(14)
        ytick.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.7))

    # Plus Annotation
    x = 3 * np.pi / 4
    plt.annotate(r'$(sin(\frac{3\pi}{4}),\frac{1}{\sqrt{2}})$',
                 xy=(x, np.sin(x)),
                 xycoords='data',
                 xytext=(+20, +20),
                 textcoords='offset points',
                 fontsize=16,
                 arrowprops=dict(facecolor='red', headwidth=8, width=2))

    plt.plot(X, F1, label="$sin(x)$")
    plt.legend(loc="lower left")
    # plt.legend(loc="best")
    plt.show()


if __name__ == '__main__':
    plot_01()
    # plot_02()
    # plot_03()
