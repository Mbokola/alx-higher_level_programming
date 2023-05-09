#!/usr/bin/python3
n = 0
for i in range(122, 96, -1):
    if (n % 2):
        i -= 32
    n += 1
    print(f"{chr(i)}", end="\n" if i == 65 else "")
