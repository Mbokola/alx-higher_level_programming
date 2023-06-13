#!/usr/bin/python3
""" 2-append_write module """


def append_write(filename="", text=""):
    """ Appends to a file, creates if non-existent """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
