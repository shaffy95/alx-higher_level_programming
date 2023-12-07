#!/usr/bin/python3

def search_replace(my_list, search, replace):
    x = []

    for y in my_list:
        if y == search:
            x.append(replace)
        else:
            x.append(y)

    return (x)
