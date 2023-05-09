#!/usr/bin/python3
for i in range(9):
    for a in range(i + 1, 10):
        print("{}{}".format(i, a), end="")
        if (i != 8 or a != 9):
            print(", ", end="")
        a += 1
    i += 1
