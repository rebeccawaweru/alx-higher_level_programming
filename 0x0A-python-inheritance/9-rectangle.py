#!/usr/bin/python3

"""Define a class Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Representing the Geometry"""

    def __init__(self, width, height):
        """Initialize a new rectangle
        Arguments:
        width: the width of the rectangle
        height: the height of the rectangle
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def __str__(self):
        """String representation of an instance"""
        return "[{}] {:d}/{:d}".format(type(self).__name__, self.__width, self.__height)

    def area(self):
        """Return the area of the rectangle"""
        return self.__width * self.__height
