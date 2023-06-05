#!/usr/bin/python3

"""Define a class Rectangle"""


class Rectangle:
    """Representing a rectangle
    Attribute:
    number_of_instances: number of rectangle instances.
    Must be an integer"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializing a new rectangle
        Arguments:
        width- the width of the rectangle. Must be an integer
        height- the height of the rectangle. Must be an integer
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get /set the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get/set the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        """Return the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Return rectangle string object"""
        if self.__width == 0 or self.__height == 0:
            return ""
        ob_rectangle = []
        for j in range(self.__height):
            [ob_rectangle.append('#') for a in range(self.__width)]
            if j != self.__height - 1:
                ob_rectangle.append("\n")
        return ("".join(ob_rectangle))

    def __repr__(self):
        """Return the string representation"""
        str_rectangle = "Rectangle(" + str(self.__width)
        str_rectangle += ", " + str(self.__height) + ")"
        return (str_rectangle)

    def __del__(self):
        """Print string at every delete action"""
        type(self).number_of_instances -= 1
        print("By rectangle...")
