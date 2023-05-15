#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    [print("{}".format(*row), end="\n") for row in matrix]
