#!/usr/bin/python3
""" module for printing squares """


def print_square(size):
    """ function for printing a square ou of # """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for no in range(size):
        print("#" * size)
