#!/usr/bin/env python3
# coding=utf-8

import numpy as np
from random import random

"""
Pocket Algorithm
"""


def sigmod(a, threshold=0):
    return 1 if a - threshold > 0 else -1


def pocket_learning(dataset, loop=1000):
    X = dataset[:, 0:-1]
    Y = np.array(dataset[:, -1], dtype=int)
    rows, cols = X.shape

    W = np.zeros((1, cols))[0]
    loop_times = 0
    while loop_times < loop:
        _W = W.copy()
        is_changed = False
        i = int(random() * rows)
        if sigmod(W.dot(X[i].transpose())) != Y[i]:
            _W += Y[i] * X[i]
            is_changed = True
        if not is_changed:
            continue
        """
        if _W takes fewer mistake than W, then, replace W by _W.
        """
        errs_count, new_errs_count = 0, 0
        for j in range(rows):
            if sigmod(W.dot(X[j].transpose())) != Y[j]:
                errs_count += 1
            if sigmod(_W.dot(X[j].transpose())) != Y[j]:
                new_errs_count += 1
        if new_errs_count < errs_count:
            W = _W.copy()
        loop_times += 1
    return W

if __name__ == '__main__':
    dataset = np.genfromtxt('pocket_data.dat')
    W = pocket_learning(dataset, loop=1000)
    print(W)