"""
Module for calculating the geometric mean.

:author: Toto Titi <toto.titi@is.mpg.de>
"""


def calculate_geomean(seq):
    """
    Function calculating the geometric mean of a sequence.

    :param iterable seq: Sequence
    :return: Geometric mean
    :rtype: float
    """
    n = len(seq)
    if not n:
        raise ValueError("Sequence must have a least one element.")
    if any(e < 0 for e in seq):
        raise TypeError("Only positive numbers are allowed.")

    product = 1
    for e in seq:
        product = e * product

    return product ** (1 / n)
