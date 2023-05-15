#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    j = 0
    for i in my_list:

        if (i % 2):
            my_list[j] = False
        my_list[j] = True
    return (my_list)
