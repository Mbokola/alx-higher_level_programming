#!/usr/bin/Python3
'''
- roman_to_int - function that converts a Roman numeral to an integer.

- You can assume the number will be between 1 to 3999.
- must return an integer
- If the roman_string is not a string or None, return 0
'''


def roman_to_int(roman_string):
    # Check if roman_string is None or not a string
    if roman_string is None or type(roman_string) != str:
        return 0
    # Craete a dictionary of roman values
    ref = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
    # Check if roman String
    for i in roman_string.upper():
        if i not in ref:
            return 0
    length = len(roman_string)
    # Check for lowercase roman string
    new = roman_string.upper()
    # Check if only 1 roman charcter
    if (length == 1):
        return ref[new]
    conversion = 0
    i = 0
    # Iterate string length - 1 times
    while i < length - 1:
        # Handle IX/XI situations
        if ref[new[i]] >= ref[new[i + 1]]:
            conversion += ref[new[i]]
            i += 1
        else:
            conversion += (ref[new[i + 1]] - ref[new[i]])
            i += 2
    # Make sure we get every character
    if (i < length):
        conversion += ref[new[i]]
    # Return conversion
    return conversion
