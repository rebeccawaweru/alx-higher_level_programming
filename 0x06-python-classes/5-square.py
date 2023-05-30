#!/usr/bin/python3

"""Define class Square"""


class Square:
    """Representing a square."""

    def __init__(self, size=0):
        """A new square
        Args:
        size - integer size of the square
        """
        self.size = size

    @property
    def size(self):
        """current value of the size"""
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

    def my_print(self):
        """Print square with #"""
        for j in range(0, self.__size):
            [print("#", end="") for y in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
