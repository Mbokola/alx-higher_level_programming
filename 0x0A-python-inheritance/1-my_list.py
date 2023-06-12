#!/usr/bin/python3
""" 1-my_list module """


class MyList(list):
    """ Subclass of list """
    def print_sorted(self):
        sortedl = sorted(self)
        print(sortedl)
