#!/usr/bin/python3
"""Define a new Class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Representing a Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializing a new instance of class Rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def height(self):
        """Define getter/setter methods"""
        return self.__height

    @height.setter
    def height(self, value):
        """Get / set the height value of the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def width(self):
        """Define getter/setter methods"""
        return self.__width

    @width.setter
    def width(self, value):
        """Get / set the width value of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def x(self):
        """Define getter/setter methods"""
        return self.__x

    @x.setter
    def x(self, value):
        """Get / set value of x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Define getter / setter methods"""
        return self.__y

    @y.setter
    def y(self, value):
        """Get /set the value of y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
