#!/usr/bin/python3
""" A class Rectangle that defines a rectangle """


class Rectangle:
    """
    initialize class attributes and methods
    """
    def __init__(self, width=0, height=0):
        """ Instantiation with optional width and height """
        self.height = height
        self.width = width

    def __str__(self):
        string = ""
        for _ in range(self.height):
            string += "#" * self.width + '\n'
        return string.rstrip('\n')

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        print("Bye rectangle...")

    @property
    def height(self):
        """ Retrieve the height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Modifiy the height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """ Retrieve the width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Modify the width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """ Calculate the area """
        return self.__width * self.__height

    def perimeter(self):
        """ calculates perimeter, returns 0 if width or height equals 0 """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
