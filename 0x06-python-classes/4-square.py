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

    @property
    def size(self):
        """ Getter function """
        return self.__size

    @size.setter
    def size(self, value):
        """ Setter function """
        if type(value) != int:
            raise TypeError("Size must be an integer")
        if value < 0:
            raise ValueError("Size must be >= 0")
        self.__size = value

    def area(self):
        """ Calulates area of a square """
        s = self.__size
        return s * s
