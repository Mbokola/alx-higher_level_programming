#!/usr/bin/Python3
'''
Write a function that prints a dictionary by ordered keys.
- You can assume that all keys are strings
- Keys should be sorted by alphabetic order
- Only sort keys of the first level (don’t sort keys of a dictionary inside the main dictionary)
- Dictionary values can have any type
- You are not allowed to import any module
'''


def print_sorted_dictionary(a_dictionary):
    sorted_dict = {k: a_dictionary[k] for k in sorted(a_dictionary)}
    print(sorted_dict, end='\n')
