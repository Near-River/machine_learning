#!/usr/bin/env python3
# coding=utf-8

import numpy as np
import numpy.linalg as lg
import matplotlib.pyplot as plt

"""
Linear Regression Algorithm
"""


def plot_data(dataset, W_Lin):
    X = dataset[:, 0:-1]
    Y = dataset[:, -1]

    plt.figure()
    # Plot the points
    plt.plot(X, Y, '*')
    # Plot the linear regression line
    X_Lin = np.linspace(0, 25, 1000)[:, np.newaxis]
    Y_Lin = np.dot(np.hstack((np.ones((1000, 1)), X_Lin)), W_Lin)
    plt.plot(X_Lin, Y_Lin)
    plt.show()


def linear_regression_learning(dataset):
    X = dataset[:, 0:-1]
    rows, cols = X.shape
    X = np.hstack((np.ones((rows, 1)), X))
    Y = dataset[:, -1]

    X, Y = np.mat(X), np.mat(Y).transpose()
    W = lg.inv(X.transpose() * X) * X.transpose() * Y
    return W


if __name__ == '__main__':
    dataset = np.genfromtxt('linear_regression_data.txt', delimiter=',')
    W_Lin = linear_regression_learning(dataset)
    plot_data(dataset, W_Lin)
