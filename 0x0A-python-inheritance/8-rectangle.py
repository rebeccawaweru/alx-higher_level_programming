#!/usr/bin/python3

"""Define class Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """New rectangle instance"""

    def __init__(self, width, height):
        """Initializing a new rectangle
        Arguments:
        width: the width
        height: the height
        """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
