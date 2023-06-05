#!/usr/bin/python3
""" A class Rectangle that defines a rectangle """


class Rectangle:
    """
    initialize class attributes and methods
    """
    def __init__(self, width=0, height=0):
        """ Instantiation with optional width and height """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def height(self):
        """ Retrieve the height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Modifiy the height """
        self.__height = value

    @property
    def width(self):
        """ Retrieve the width """
        return self.width

    @width.setter
    def width(self, value):
        """ Modify the width """
        self.__width = value
