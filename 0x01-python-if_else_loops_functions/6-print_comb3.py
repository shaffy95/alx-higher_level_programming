#!/usr/bin/python3
for value in range(9):
    for num in range(value + 1, 10):
        if value == 8 and num == 9:
            print(f"{value}{num}")
        else:
            print(f"{value}{num}, ", end='')

