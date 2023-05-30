#!/usr/bin/python3
""" A simple Class """


class Square:
    """ The Square Class """
    def __init__(self, size=0):
        """ Class Instantiation """
        self.size = size

    def area(self):
        """ Calulates area of a square """
        s = self.__size
        return s * s

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
