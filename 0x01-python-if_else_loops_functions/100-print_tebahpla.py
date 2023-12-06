#!/usr/bin/python3
for value in range(122, 96, -1):
    if value % 2 != 0:
        value -= 32
    print("{}".format(chr(value)), end='')
