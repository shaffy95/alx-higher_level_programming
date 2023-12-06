#!/usr/bin/python3
for value in range(97, 123):
    if chr(value) != 'q' and chr(value) != 'e':
        print('{:c}'.format(value), end='')
