#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    value_list = []

    for value in my_list:
        if value % 2 == 0:
            value_list.append(True)
        else:
            value_list.append(False)
    return (value_list)
