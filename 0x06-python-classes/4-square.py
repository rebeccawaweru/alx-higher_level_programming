#!/usr/bin/python3

"""Define class Square"""


class Square:
    """The square"""

    def __init__(self, size=0):
        """A new square
        Args:
        size - integer size of the square
        """
        self.__size = size

    @property
    def size(self):
        """acquire current size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return area of the square"""
        return (self.__size * self.__size)
