#!/usr/bin/python3
""" 2-is_same_class module """


def is_same_class(obj, a_class):
    """ Check if object ia an instance of a class """
    return type(obj) is a_class
