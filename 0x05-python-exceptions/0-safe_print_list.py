#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    j = 0
    try:
        for i in my_list:
            if (x):
                print(x, end="")
                x -= 1
                j += 1
        print()
        return j
    except Exception:
        print("Exeption raised")
