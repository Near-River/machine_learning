import matplotlib.pyplot as plt


def plot_01():
    days = list(range(1, 9))
    celsius_values = [25.6, 24.1, 26.7, 28.3, 27.5, 30.5, 32.8, 33.1]
    plt.plot(days, celsius_values)
    plt.xlabel('Day')
    plt.ylabel('Degrees Celsius')
    plt.show()


def plot_02():
    days = list(range(1, 9))
    celsius_min = [19.6, 24.1, 26.7, 28.3, 27.5, 30.5, 32.8, 33.1]
    celsius_max = [24.8, 28.9, 31.3, 33.0, 34.9, 35.6, 38.4, 39.2]
    plt.xlabel('Day')
    plt.ylabel('Degrees Celsius')
    plt.plot(days, celsius_min,
             days, celsius_min, "oy",
             days, celsius_max,
             days, celsius_max, "or")
    # Define the range of Axes
    xmin, xmax, ymin, ymax = 0, 10, 15, 45
    plt.axis([xmin, xmax, ymin, ymax])
    plt.show()


if __name__ == '__main__':
    plot_01()
    # plot_02()
