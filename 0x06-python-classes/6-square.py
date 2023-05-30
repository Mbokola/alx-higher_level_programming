#!/usr/bin/python3
""" A simple Class """


class Square:
    """ The Square Class """
    def __init__(self, size=0, position=(0, 0)):
        """ Class Instantiation """
        self.__size = size
        self.__position = position

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
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        s = self.__size
        if (not s):
            print()
        while s:
            print(" " * self.position[0] + "#" * self.__size)
            s -= 1

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value(0)) != int and type(value(1)) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value(0) < 0 or value(1) < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
