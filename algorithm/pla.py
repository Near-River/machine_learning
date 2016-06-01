#!/usr/bin/env python3
# coding=utf-8

import numpy as np
import matplotlib.pyplot as plt
from random import random

"""
Perception Learning Algorithm
"""


def plot_data(dataset, W):
    Y = np.array(dataset[:, -1], dtype=int)
    X_pos = (dataset[Y == -1])[:, 0:-1]
    X_neg = (dataset[Y == 1])[:, 0:-1]

    plt.figure()
    # Plot the points
    plt.plot(X_pos[:, 0], X_pos[:, 1], 'o')
    plt.plot(X_neg[:, 0], X_neg[:, 1], 'x')
    # Plot the dividing line
    X = np.linspace(0, 1, 1000)
    slope = -1 * W[0] / W[1]
    plt.plot(X, slope * X)
    plt.show()
    plt.close()


def sigmod(a, threshold=0):
    return 1 if a - threshold > 0 else -1


def pla_learning(dataset):
    X = dataset[:, 0:-1]
    Y = np.array(dataset[:, -1], dtype=int)
    rows, cols = X.shape
    W = np.zeros((1, cols))[0]
    while True:
        is_changed = False
        i = int(random() * rows)
        if sigmod(W.dot(X[i].transpose())) != Y[i]:
            W += Y[i] * X[i]
            is_changed = True
        if not is_changed:
            continue
        count = 0
        for i in range(rows):
            if sigmod(W.dot(X[i].transpose())) == Y[i]:
                count += 1
        if count == rows:
            break
    return W


if __name__ == '__main__':
    dataset = np.genfromtxt('pla_data.dat')
    W = pla_learning(dataset)
    plot_data(dataset, W)
