#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keysDelete = [key for key, n in a_dictionary.items() if n == value]
    for key in keysDelete:
        del a_dictionary[key]
    return a_dictionary
