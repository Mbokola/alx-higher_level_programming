#!/usr/bin/python3
""" 9-student module """


class Student:
    """ The Student class """
    def __init__(self, first_name, last_name, age):
        """ Class initialization """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Dictionary representation of class atrributes """
        if attrs is not None:
            mydict = {}
            if ("first_name" in attrs):
                mydict["first_name"] = self.first_name
            if ("last_name" in attrs):
                mydict["last_name"] = self.last_name
            if ("age" in attrs):
                mydict["age"] = self.age
            return mydict
        return self.__dict__
