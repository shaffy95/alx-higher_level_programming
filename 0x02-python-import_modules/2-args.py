#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    num_value = len(sys.argv) - 1
    if num_value == 0:
        print("0 arguments.")
    elif num_value == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(num_value))
    for value in range(num_value):
        print("{}: {}".format(value + 1, sys.argv[value + 1]))
