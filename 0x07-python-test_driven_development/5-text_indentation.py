#!/usr/bin/python3
""" 5-text_indentation.py """


def text_indentation(text):
    """
    function that prints a text with 2 new lines after each of these
    characters: ., ? and :
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    characters = ['.', '?', ':']
    index = 0
    current = 0

    for char in text:
        if char in characters:
            print(f"{text[index:current + 1]}\n\n", end="")
            index = current + 1
        current += 1
        if index < len(text) and text[index].isspace():
            index += 1
    if index < len(text):
        print(f"{text[index:]}", end="")
