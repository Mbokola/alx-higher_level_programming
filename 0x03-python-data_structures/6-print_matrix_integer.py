#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        i = 1
        for digit in row:
            print("{:d}".format(digit), end=' ' if i < len(row) else '')
            i += 1
        print()
