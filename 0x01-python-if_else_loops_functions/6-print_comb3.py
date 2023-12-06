#!/usr/bin/python3
for value in range(0, 10):
    for num in range(value + 1, 10):
        if value == 8 and num == 9:
            print('89')
        else:
            print('{}{}, '.format(value, num), end='')
