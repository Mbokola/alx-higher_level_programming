#!/usr/bin/python3
""" 12-pascal_triangle module """


def pascal_triangle(n):
    """ Creates pascals trinangle of size n """

    # create an empty list
    mylist = []
    # if n <= 0 return empty list
    if n <= 0:
        return mylist
    # if n == 1 list = [1] return list
    if n == 1:
        return [[1]]
    # Default list = [[1], [1, 1]]
    mylist = [[1], [1, 1]]
    # n -= 2 since list initialised with 2 values
    n -= 2
    # while n
    while n:
        # Use list comprehension
        x = [
            x + mylist[-1][i + 1]
            for i, x in enumerate(mylist[-1])
            if i < len(mylist[-1]) - 1
        ]
        # insert 1 at beggining and end of x
        x.insert(0, 1)
        x.append(1)
        # Append x to list
        mylist.append(x)
        n -= 1
    # return list
    return mylist
