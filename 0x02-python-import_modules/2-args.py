#!/usr/bin/python3
import sys
if (__name__ == '__main__'):
    args = len(sys.argv)
    if (args == 1):
        print('0 arguments.')
    else:
        if (args == 2):
            print(f"{args - 1} argument:")
        else:
            print(f"{args - 1} arguments:")
        for i in range(1, args):
            print(f"{i}: {sys.argv[i]}")
