#!/usr/bin/python3
""" 4-print_square.py module """


def print_square(size):
    """ function that prints a square with the character # """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(0, size):
        print("#" * size)
