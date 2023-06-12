#!/usr/bin/python3

Rectangle = __import__('9-rectangle').Rectangle
"""Define class Square"""


class Square(Rectangle):
    """ Implemting class square"""

    def __init__(self, size):
        """Initializing a new square"""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
