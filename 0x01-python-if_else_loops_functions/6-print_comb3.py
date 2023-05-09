#!/usr/bin/python3
for i in range(9):
    print(i, end="")
    for a in range(i + 1, 10):
        if (i != 8 and a != 9):
            print("{}, ".format(i))
