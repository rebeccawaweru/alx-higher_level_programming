#!/usr/bin/python3

"""Define the class Square"""


class Square:
    """Representing a square"""
    def __init__(self, size=0, position=(0, 0)):
        """A new square is initialized
        Args:
        size - integer size of the square
        position - location of the new square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Acquire the size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Acquire the location of the square"""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(number, int) for number in value) or
                not all(number >= 0 for number in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return area of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        """Printing the square with #"""
        if self.__size == 0:
            print("")
            return

        [print("") for x in range(0, self.__position[1])]
        for x in range(0, self.__size):
            [print(" ", end="") for a in range(0, self.__position[0])]
            [print("#", end="") for a in range(0, self.__size)]
            print("")
