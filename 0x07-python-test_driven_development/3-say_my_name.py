#!/usr/bin/python3

""" say_my_name
Prints the first and last name
Takes two arguments: first name and last name
Other type raise TypeError
"""


def say_my_name(first_name, last_name=""):
    """say_my_name
    Prints the first and the last name

    Arguments:
    first_name - must be a string
    last_name - must be a string

    Raises:
    TypeError: if first_name or last_name is not a string
    """
    if first_name is None and last_name is None:
        raise TypeError("missing arguments")
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
