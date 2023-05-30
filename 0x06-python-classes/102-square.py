#!/usr/bin/python3

"""Defining the square"""


class Square:
    """Representation of a square"""

    def __init__(self, size=0):
        """A new square
        Args:
        size: size of the square, should be an integer
        """
        self.size = size

    @property
    def size(self):
        """Acquire size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square"""
        return (self.__size * self.__size)

    def __eq__(self, other):
        """Define the comparison to the square"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Define the is not != comparison to the square"""
        return self.area() != other.area()

    def __lt__(self, other):
        """Defining the less than comaprison to the square"""
        return self.area() < other.area()

    def __gt__(self, other):
        """Define the greater than comparison to the square"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define the greater than or equal comparison to a square"""
        return self.area() >= other.area()
