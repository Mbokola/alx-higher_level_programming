#!/usr/bin/python3
""" 10-square module """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ The sqaure class """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        Rectangle.__init__(self, size, size)
        Rectangle.area(self)
