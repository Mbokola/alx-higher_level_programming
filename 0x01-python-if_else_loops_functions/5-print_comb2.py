#!/usr/bin/python3
for i in range(10):
    for a in range(0, 10):
        if i != 9 or a != 9:
            print("{}{}, ".format(i, a), end="")
        else:
            print("{}{}".format(i, a), end="")
        a += 1
    i += 1
