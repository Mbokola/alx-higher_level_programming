#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new = []
    temp_result = 0
    for i in range(0, list_length):
        try:
            temp_result = my_list_1[i] / my_list_2[i]
        except TypeError:
            temp_result = 0
            print("wrong type")
        except ZeroDivisionError:
            temp_result = 0
            print("division by 0")
        except IndexError:
            temp_result = 0
            print("out of range")
        finally:
            pass
        new.append(temp_result)

    if len(my_list_1) > list_length:
        new.extend([0] * (len(my_list_1) - list_length))

    return new
