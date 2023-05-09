#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    y = number % (-10)
else:
    y = number % 10

if y > 5:
    print("Last digit of {} is {} and is greater than {}".format(number, y, 5))
elif y == 0:
    print("Last digit of {} is {} and is {}".format(number, y, 0))
elif y < 6 and y != 0:
    print("Last digit of {} is {} and "
          "is less than 6 and not 0".format(number, y))
