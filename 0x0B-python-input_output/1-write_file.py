#!/usr/bin/python3
""" 1-write_file module """


def write_file(filename="", text=""):
    """ Write to file, create if non-existent else overwrite"""
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
