#!/usr/bin/env python3
# coding=utf-8

import numpy as np
import matplotlib.pyplot as plt
from math import exp

"""
Logistic Regression Algorithm
"""


def plot_data(dataset, W):
    Y = np.array(dataset[:, -1], dtype=int)
    X_pos = (dataset[Y == 0])[:, 0:-1]
    X_neg = (dataset[Y == 1])[:, 0:-1]

    plt.figure()
    # Plot the points
    plt.plot(X_pos[:, 0], X_pos[:, 1], 'o')
    plt.plot(X_neg[:, 0], X_neg[:, 1], 'x')
    # Plot the logistic devision line

    plt.show()


def sigmoid(Z):
    if type(Z) == float or type(Z) == int:
        return 1 / (1 + exp(-1 * Z))
    if type(Z) == np.ndarray:
        return 1 / (1 + np.exp(-1 * Z))


def logistic_regression_learning(dataset):
    X = dataset[:, 0:-1]
    rows, cols = X.shape
    X = np.hstack((np.ones((rows, 1)), X))
    Y = np.array(dataset[:, -1], dtype=int)[:, np.newaxis]
    Y[Y == 0] = -1

    # Initial W (Wo = 0)
    W = np.zeros((cols + 1, 1))
    # Definite the fixed learning rate
    theta = 0.001
    N = rows
    count, loop_times = 0, 400

    while count < loop_times:
        # Derviation the derviative of In-sample-error
        derviate = (1 / N) * np.sum(sigmoid(-1 * Y * X.dot(W)) * (-1 * Y * X), axis=0)
        if (derviate == np.zeros((cols + 1,))).all():
            break
        # Update the W
        W -= theta * derviate[:, np.newaxis]
        count += 1

    # Statistic accuracy of the problems
    res = np.dot(X, W)
    # print(res)
    positive_true = np.count_nonzero(Y[res >= 0.5] == 1)
    negitive_false = np.count_nonzero(Y[res < 0.5] == -1)
    print('Accuracy: %d' % (positive_true + negitive_false))

    return W


if __name__ == '__main__':
    dataset = np.genfromtxt('logistic_regression_data.txt', delimiter=',')
    W = logistic_regression_learning(dataset)
    print(W)
    # plot_data(dataset, W)
