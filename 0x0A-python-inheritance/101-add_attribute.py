#!/usr/bin/python3
""" 101-add_attribute module """


def add_attribute(obj, attr, value):
    """ Set attribute method """
    if hasattr(obj, '__dict__'):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
