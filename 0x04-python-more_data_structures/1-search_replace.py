#!/usr/bin/Python3
'''
- search_replace - function that replaces all occurrences of an element by
another in a new list.
- my_list is the initial list
- search is the element to replace in the list
- replace is the new element
- You are not allowed to import any module
'''


def search_replace(my_list, search, replace):
    # Create a lambda function that replaces occurences of search
    # Return new list
    return list(map(lambda num: replace if num == search else num, my_list))
