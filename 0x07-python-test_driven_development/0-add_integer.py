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
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float) and (a == float('inf') or a == float('-inf')):
        raise OverflowError("Float overflow")
    if isinstance(b, float) and (b == float('inf') or b == float('-inf')):
        raise OverflowError("Float overflow")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if a != int(a) or b != int(b):
        raise ValueError("cannot convert float NaN to integer")

    return a + b
