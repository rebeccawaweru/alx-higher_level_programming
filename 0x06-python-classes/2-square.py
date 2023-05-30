#!/usr/bin/python3

"""Define class Square"""


class Square:
    """A new square
    Args:
    size: must be an integer and greater than 0
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
