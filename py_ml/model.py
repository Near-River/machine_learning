#!/usr/bin/env python
# coding=utf-8
from sklearn.cluster import KMeans
from sklearn.externals import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pylab import *


def main():
    df = pd.read_csv("final_data_new.csv", header=0)
    columns = list(df.columns)[3:]
    print(str(columns))
    cols = ["Registered Captial", "Project Investment", "number of team", "number of shareholders",
            "Judges score", "Judges Vote", "Entrepreneurship subsidies", "Service Lines", "Support Line",
            "Financing situation", "Financing Plan",
            "Professional Background", "Technology Experience", "Competitive Advantage", "Stage of Product",
            "University-Enterprise Cooperation",
            "The core technology development time", "If there is a success story",
            "Technical director of degree", "Technical director of the resume", "Marketing director resume",
            "The highest record of formal schooling", ]
    x = np.array(df[columns[0]])
    for i in range(1, len(columns)):
        current_X = np.array(df[columns[i]])
        x = np.column_stack((x, current_X))
    print(str(x.shape))
    n = 3
    clf = KMeans(n_clusters=n)
    s = clf.fit(x)
    y = np.array(clf.labels_)
    for i in range(x.shape[1]):
        for j in range(n):
            plt.scatter(x[y == j, i], y[y == j], c=np.concatenate((np.random.random(3), np.array([0.5]))))
        plt.title(cols[i])
        plt.savefig("pic_" + str(i) + ".png", dpi=300)
        plt.close()
    print(str(y))


if __name__ == '__main__':
    main()
