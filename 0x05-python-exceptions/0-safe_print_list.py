#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    j = 0
    for i in my_list:
        if x:
            print(i)
            x -= 1
            j += 1
