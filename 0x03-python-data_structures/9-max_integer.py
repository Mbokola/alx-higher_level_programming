#!/usr/bin/python3
def max_integer(my_list=[]):
    if not len(my_list):
        return None
    sort_list = sorted(my_list)
    return (sort_list[-1])
