#!/usr/bin/python3
""" 0-read_file module """


def read_file(filename=""):
    """ Read a file """
    with open(filename, encoding="UTF8") as f:
        print(f.read(), end='')
