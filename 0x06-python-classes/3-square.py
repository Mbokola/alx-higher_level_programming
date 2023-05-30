#!/usr/bin/python3
""" A simple Class """


class Square:
    """ The Square Class """
    def __init__(self, size=0):
        """ Class Instantiation """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calulates area of a square"""
        s = self.__size
        return s * s
