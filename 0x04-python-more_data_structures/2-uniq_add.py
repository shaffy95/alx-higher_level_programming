#!/usr/bin/python3
def uniq_add(my_list=[]):
    matrix_list = 0
    for x in set(my_list):
        matrix_list += x
    return matrix_list
