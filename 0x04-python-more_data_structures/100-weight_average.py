#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list and len(my_list):
        value = 0
        current_value = 0
        for items in my_list:
            value += (items[0] * items[1])
            current_value += (items[1])
        return (value/current_value)
    return 0
