#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    j = 0
    new_list = my_list.copy()
    for i in new_list:
        if (i % 2):
            new_list[j] = 0
            j += 1
            continue
        new_list[j] = 1
        j += 1
    return (new_list)
