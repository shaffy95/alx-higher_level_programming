#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    lastdigit = number % -10
else:
    lastdigit = number % 10
if lastdigit < 6:
    print("Last digit of {:d} is {:d} and is less than 6"
          .format(number, lastdigit))
elif lastdigit > 5 and lastdigit != 0:
    print("Last digit of {:d} is {:d} and is greater than 5 and not 0"
          .format(number, lastdigit))
else:
    print("Last digit of {:d} is 0 and is 0".format(number))
