#!/usr/bin/Python3
'''
- square_matrix_simple - function that computes the square value of all
integers of a matrix.
- matrix is a 2 dimensional array
- Returns a new matrix:
- Same size as matrix
- Initial matrix should not be modified
- You are not allowed to import any module
- You are allowed to use regular loops, map, etc.
- Each value should be the square of the value of the input
'''


def square_matrix_simple(matrix=[]):
    # Create a lambda function that calculates square of a number
    # lambda num: num ** 2
    # Nest the lambda function inside map function
    # Return new_list
    return list(map(lambda row: list(map(lambda num: num**2, row)), matrix))
