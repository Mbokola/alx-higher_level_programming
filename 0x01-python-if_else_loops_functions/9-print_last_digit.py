#!/usr/bin/python3
def print_last_digit(number):
    a = (number % 10)
    if (a < 0):
        a *= -1
    print(a, end="")
    return a
