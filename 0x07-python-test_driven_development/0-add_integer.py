#!/usr/bin/python3

""" add_integer
Adds two integers and return the sum
Number that are floats are converted to integers
Other types are raise a TypeError
"""


def add_integer(a, b=98):
    """ add_integer - add two integer numbers a,b
    Return: sum
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
