#!/usr/bin/env python3
# coding=utf-8

"""
Definition of Synthetical Data
"""

from np_probability import cartesian_choice, weighted_cartesian_choice

weighted_firstnames = [("John", 80), ("Eve", 70), ("Jane", 2),
                       ("Paul", 8), ("Frank", 20), ("Laura", 6),
                       ("Robert", 17), ("Zoe", 3), ("Roger", 8),
                       ("Simone", 9), ("Bernard", 8), ("Sarah", 7),
                       ("Yvonne", 11), ("Bill", 12), ("Bernd", 10)]
weighted_surnames = [('Singer', 2), ('Miles', 2), ('Moore', 5),
                     ('Looper', 1), ('Rampman', 1), ('Chopman', 1),
                     ('Smiley', 1), ('Bychan', 1), ('Smith', 150),
                     ('Baker', 144), ('Miller', 87), ('Cook', 5),
                     ('Joyce', 1), ('Bush', 5), ('Shorter', 6),
                     ('Klein', 1)]
firstnames, weights = zip(*weighted_firstnames)
wsum = sum(weights)
weights_firstnames = [x / wsum for x in weights]  # normalize the weights
surnames, weights = zip(*weighted_surnames)
wsum = sum(weights)
weights_surnames = [x / wsum for x in weights]
weights = (weights_firstnames, weights_surnames)


def synthesizer(data, weights=None, format_func=None, repeats=True):
    """
    "data" is a tuple or list of lists or tuples containing the data.

    "weights" is a list or tuple of lists or tuples with the
    corresponding weights of the data lists or tuples.

    "format_func" is a reference to a function which defines
    how a random result of the creator function will be formated.
    If None,the generator "synthesize" will yield the list "res".

    If "repeats" is set to True, the output values yielded by
    "synthesize" will not be unique.
    """
    if not repeats:
        memory = set()

    def choice(data, weights):
        if weights:
            return weighted_cartesian_choice(*zip(data, weights))
        else:
            return cartesian_choice(*data)

    def synthesize():
        while True:
            res = choice(data, weights)
            if not repeats:
                sres = str(res)
                while sres in memory:
                    res = choice(data, weights)
                    sres = str(res)
                memory.add(sres)
            if format_func:
                yield format_func(res)
            else:
                yield res

    return synthesize


if __name__ == '__main__':
    recruit_employee = synthesizer((firstnames, surnames),
                                   weights=weights,
                                   format_func=lambda x: " ".join(x),
                                   repeats=False)
    employee = recruit_employee()
    for _ in range(10):
        print(next(employee))
