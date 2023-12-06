#!/usr/bin/python3
def uppercase(str):
    for value in str:
        if ord(value) >= 97 and ord(value) <= 122:
            value = chr(ord(value) - 32)
        print("{}".format(value), end="")
    print()
