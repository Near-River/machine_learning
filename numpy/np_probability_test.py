#!/usr/bin/env python3
# coding=utf-8

from collections import Counter
from np_probability import weighted_choice

"""
Numpy and Probability
"""


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
