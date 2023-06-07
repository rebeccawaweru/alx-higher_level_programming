#!/usr/bin/python3

""" print_square
Prints a square with #
Has one argument size 
"""

def print_square(size):
    """Print a square with #
    Args:
    size - integer size of square
    """
    if size is None:
        raise TypeError("missing argument")
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if size > 0:
        for a in range(size):
            print("#" * size)
