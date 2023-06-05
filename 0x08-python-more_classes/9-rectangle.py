#!/usr/bin/python3
""" A class Rectangle that defines a rectangle """


class Rectangle:
    """
    initialize class attributes and methods
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Instantiation with optional width and height """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    def __str__(self):
        string = ""
        for _ in range(self.height):
            string += Rectangle.print_symbol * self.width + '\n'
        return string.rstrip('\n')

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        area1 = rect_1.height * rect_1.width
        area2 = rect_2.height * rect_2.width

        if area1 == area2:
            return rect_1
        if area1 > area2:
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return (cls(size, size))
