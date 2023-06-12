#!/usr/bin/python3

Rectangle = __import__('9-rectangle').Rectangle

"""Defining class Rectangle"""


class Square(Rectangle):
    """Representing a square"""
    def __init__(self, size):
        """Initializing new square"""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """The area of the square"""
        return self.__size ** 2
