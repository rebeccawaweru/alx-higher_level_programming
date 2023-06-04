#!/usr/bin/python3

def say_my_name(first_name, last_name=""):
    """
    Prints the first and the last name

    Arguments:
    first_name - must be a string
    last_name - must be a string

    Raises:
    TypeError: if first_name or last_name is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
