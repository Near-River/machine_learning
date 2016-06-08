#!/usr/bin/env python3
# coding=utf-8

import numpy as np
import numpy.linalg as lg
import matplotlib.pyplot as plt

"""
Logistic Regression Algorithm
"""


def plot_data(dataset, W_Lin):
    X = dataset[:, 0:-1]
    Y = np.array(dataset[:, -1], dtype=int)

    plt.figure()
    # Plot the points
    plt.plot(X, Y, '*')
    # Plot the logistic regression line
    X_Lin = np.linspace(0, 25, 1000)[:, np.newaxis]
    Y_Lin = np.dot(np.hstack((np.ones((1000, 1)), X_Lin)), W_Lin)
    plt.plot(X_Lin, Y_Lin)
    plt.show()


def logistic_regression_learning(dataset):
    X = dataset[:, 0:-1]
    rows, cols = X.shape
    X = np.hstack((np.ones((rows, 1)), X))
    Y = np.array(dataset[:, -1], dtype=int)
    W = np.zeros((1, cols))[0]

    X, Y = np.mat(X), np.mat(Y).transpose()

    return W


if __name__ == '__main__':
    dataset = np.genfromtxt('logistic_regression_data.txt', delimiter=',')
    W_Lin = logistic_regression_learning(dataset)
    # plot_data(dataset, W_Lin)
