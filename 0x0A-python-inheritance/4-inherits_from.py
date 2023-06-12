#!/usr/bin/python3
""" 4-inherits_from """


def inherits_from(obj, a_class):
    """ check if sub class """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
