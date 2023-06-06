#!/usr/bin/python3
""" 2-matrix_divided.py module """


def matrix_divided(matrix, div):
    """ function that divides all elements of a matrix. """
    if div == 0:
        raise ZeroDivisionError("division by zero")
    is_list_of_lists = all(isinstance(row, list) for row in matrix)
    is_valid = all(
        isinstance(num, float) or isinstance(num, int)
        for row in matrix
        for num in row
    )
    if not is_list_of_lists or not is_valid:
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    length = len(matrix[0])
    is_equal = all(len(row) == length for row in matrix)
    if not is_equal:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    return [[round(num/div, 2) for num in row] for row in matrix]
