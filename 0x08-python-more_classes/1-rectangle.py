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

    @property
    def height(self):
        """ Retrieve the height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Modifiy the height """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    @property
    def width(self):
        """ Retrieve the width """
        return self.width

    @width.setter
    def width(self, value):
        """ Modify the width """
        self.__width = value
