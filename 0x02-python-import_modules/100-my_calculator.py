#!/usr/bin/python3
import calculator_1 as calc
import sys
if (__name__ == '__main__'):
    if (len(sys.argv) != 4):
        print(f"Usage: {sys.argv[0]} <a> <operator> <b>")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    op = sys.argv[2]
    if (op == '+'):
        print(f"{a} + {b} = {calc.add(a, b)}")
    elif (op == '-'):
        print(f"{a} - {b} = {calc.sub(a, b)}")
    elif (op == '*'):
        print(f"{a} * {b} = {calc.mul(a, b)}")
    elif (op == '/'):
        print(f"{a} / {b} = {calc.div(a, b)}")
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
