#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for rowvalues in matrix:
        for value in rowvalues:
            if value == rowvalues[-1]:
                print('{:d}'.format(value), end='')
            else:
                print('{:d}'.format(value), end=' ')
        print()
