#!/usr/bin/python3
def roman_to_int(roman_string):
    if (not len(roman_string)):
        return 0
    ref = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
    total = 0
    counter = 0
    for i in roman_string:
        i = i.upper()
        if i in ref:
            total += ref[i]
            if ref[i] > counter:
                total -= counter * 2
            counter = ref[i]
        else:
            return 0
    return total
