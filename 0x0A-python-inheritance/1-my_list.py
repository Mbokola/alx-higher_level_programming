#!/usr/bin/python3
""" 1-my_list module """


class MyList(list):
    """ Subclass of list """
    def print_sorted(self):
        """ Prints out a sorted list """
        sortedl = sorted(self)
        print(sortedl)
