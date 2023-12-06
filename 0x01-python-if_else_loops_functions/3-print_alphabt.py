#!/usr/bin/python3
for value in range(97, 123):
    if chr(value) != '99' and chr(value) != '120':
        print('{:c}'.format(value), end='')
