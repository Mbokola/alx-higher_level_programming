#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    j = 0
    for i in my_list:
        if (x):
            try:
                print("{:d}".format(i), end="")
                x -= 1
                j += 1
            except Exception:
                x -= 1
                pass
    if (x):
        raise IndexError
    print()
    return j
