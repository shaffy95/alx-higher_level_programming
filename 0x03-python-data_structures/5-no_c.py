#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for value in my_string:
        if value not in 'cC':
            new_string += value
    return new_string
