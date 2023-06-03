#!/usr/bin/python3

""" say_my_name
prints the first and last name
"""


def say_my_name(first_name, last_name=""):
    """
    Arguments:
    first_name - must be a string
    last_name - must be a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
