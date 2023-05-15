#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length:
        my_tuple = (length, sentence[0])
        return my_tuple
    my_tuple = (length, None)
    return my_tuple
