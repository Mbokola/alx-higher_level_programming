#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new = []
    comb = zip(my_list_1[:list_length], my_list_2[:list_length])
    for k, v in comb:
        try:
            result = k / v
        except TypeError:
            result = 0
            print("wrong type")
        except ZeroDivisionError:
            result = 0
            print("division by 0")
        except IndexError:
            result = 0
            print("out of range")
        finally:
            new.append(result)
    return new
