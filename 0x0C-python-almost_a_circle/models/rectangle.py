#!/usr/bin/python3
""" rectangle module """
from models.base import Base


class Rectangle(Base):
    """ The Rectangle class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Class initialization """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} -\
 {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """ updates class attributes """
        attributes = ['id', 'width', 'height', 'x', 'y']
        if args:
            for attr, value in zip(attributes, args):
                setattr(self, attr, value)
        else:
            for attr in attributes:
                if attr in kwargs:
                    setattr(self, attr, kwargs[attr])

    def area(self):
        """ Calculate the area """
        return self.__width * self.__height

    def display(self):
        """ Prints the rectangle """
        print('\n' * self.__y, end='')
        print('\n'.join([' ' * self.__x + '#' *
                         self.__width for _ in range(self.__height)]))

    @property
    def width(self):
        """ width getter function """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter function """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ height getter function """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter function """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ x getter function """
        return self.__x

    @x.setter
    def x(self, value):
        """ x setter function """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ y getter function """
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter function """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def to_dictionary(self):
        """ Returns dictionary representation of Rectangle """
        return {'id': self.id, 'width': self.__width, 'height': self.__height,
                'x': self.__x, 'y': self.__y}
