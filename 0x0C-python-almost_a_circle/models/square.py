#!/usr/bin/python3
""" square module """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ The square class """
    def __init__(self, size, x=0, y=0, id=None):
        """ initialize square """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Class string representation """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """ size setter """
        return self.width

    @size.setter
    def size(self, value):
        """ Size setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Update Square attributes """
        attributes = ['id', 'size', 'x', 'y']
        if args:
            for attr, value in zip(attributes, args):
                setattr(self, attr, value)
        else:
            for attr in kwargs:
                if attr in attributes:
                    setattr(self, attr, kwargs[attr])

    def to_dictionary(self):
        """ Return Dictionary representation of Square """
        return {'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y}
