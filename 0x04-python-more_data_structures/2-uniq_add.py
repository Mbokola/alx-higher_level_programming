#!/usr/bin/Python3
'''
- uniq_add - function that adds all unique integers in a
list (only once for each integer).
- You are not allowed to import any module
'''


def uniq_add(my_list=[]):
    # use sum function and list comprehension
    return sum({num for num in my_list})
