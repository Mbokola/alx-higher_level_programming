#!/usr/bin/python3
for i in range(122, 96, -1):
    if (i % 2):
        i -= 32
    print(f"{chr(i)}", end="\n" if i == 65 else "")
