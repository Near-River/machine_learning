import numpy as np
import matplotlib.pyplot as plt

"""
Histgrams:
    It's a graphical representation of a frequency distribution of some numerical data.
    Rectangles with equal sizes in the horizontal directions have heights with the
    corresponding frequencies.
"""


def plot_01():
    gaussian_numbers = np.random.normal(size=10000)
    n, bins, patches = plt.hist(gaussian_numbers, normed=True)
    print("n: ", n, sum(n))
    print("bins: ", bins)
    for i in range(len(bins) - 1):
        print(bins[i + 1] - bins[i])
    print("patches: ", patches)
    print(patches[1])

    plt.title('Gaussian Histgram')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.show()


def plot_02():
    gaussian_numbers = np.random.normal(size=10000)
    n, bins, patches = plt.hist(gaussian_numbers,
                                bins=100,
                                normed=True,
                                stacked=True,
                                edgecolor="#6A9662",
                                color="#DDFFDD"
                                )
    print("n: ", n, sum(n))
    plt.show()


def plot_03():
    gaussian_numbers = np.random.normal(size=10000)
    n, bins, patches = plt.hist(gaussian_numbers,
                                bins=100,
                                normed=True,
                                stacked=True,
                                cumulative=True
                                )
    plt.show()


def plot_04():
    f = plt.figure()
    ax = f.add_subplot(1, 1, 1)
    ax.bar([1, 2, 3, 4], [1, 4, 9, 16])
    children = ax.get_children()
    children[1].set_color('g')
    plt.show()


def plot_05():
    years = ('2010', '2011', '2012', '2013', '2014')
    visitors = (3241, 50927, 162242, 222093, 296665 / 8 * 12)
    index = np.arange(len(visitors))
    bar_width = 1.0
    plt.bar(index, visitors, bar_width, color="green")
    plt.xticks(index + bar_width / 2, years)  # labels get centered
    plt.show()


if __name__ == '__main__':
    plot_01()
    # plot_02()
    # plot_03()
    # plot_04()
    # plot_05()
