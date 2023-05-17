#!/usr/bin/python3
def roman_to_int(roman_string):
    total = 0
    ref = dict(I=1, V=5, X=10, C=100, D=500, M=1000)
    for i in roman_string:
        if i in ref:
            total += ref[i]
    return total
