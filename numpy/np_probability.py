#!/usr/bin/env python3
# coding=utf-8

import numpy as np
from collections import Counter

"""
Numpy and Probability
"""


def find_interval(x, partition, endpoints=True):
    """ find_interval -> i
        If endpoints is True, "i" will be the index for which applies
        partition[i] < x < partition[i+1], if such an index exists.
        -1 otherwise

        If endpoints is False, "i" will be the smallest index
        for which applies x < partition[i]. If no such index exists
        "i" will be set to len(partition)
    """
    for i in range(0, len(partition)):
        if x < partition[i]:
            return i - 1 if endpoints else i
    return -1 if endpoints else len(partition)


def weighted_choice(sequence, weights):
    """
    weighted_choice selects a random element of
    the sequence according to the list of weights
    """
    x = np.random.random()
    cum_weights = [0] + list(np.cumsum(weights))
    index = find_interval(x, cum_weights)
    return sequence[index]


def process_datafile(filename):
    """ process_datafile -> (universities,
                             enrollments,
                             total_number_of_students)
        universities: list of University names
        enrollments: corresponding list with enrollments
        total_number_of_students: over all universities
    """
    universities = []
    enrollments = []
    with open(filename) as fh:
        total_number_of_students = 0
        fh.readline()  # get rid of descriptive first line
        for line in fh:
            line = line.strip()
            *praefix, undergraduates, postgraduates, total = line.rsplit()
            university = praefix[1:]
            total = int(total.replace(",", ""))
            enrollments.append(total)
            universities.append(" ".join(university))
            total_number_of_students += total
    return universities, enrollments, total_number_of_students


if __name__ == '__main__':
    universities, enrollments, total_students = process_datafile("universities_uk.txt")
    # for i in range(10):
    #     print(universities[i], enrollments[i])
    print("Total number of students onrolled in the UK: ", total_students)

    # "enroll" 100,000 fictional students.
    normalized_enrollments = [students / total_students for students in enrollments]
    outcomes = []
    for i in range(100000):
        outcomes.append(weighted_choice(universities, normalized_enrollments))
    c = Counter(outcomes)
    print(c.most_common(10))
