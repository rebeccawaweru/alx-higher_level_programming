#!/usr/bin/python3

"""Define a class Rectangle"""


class Rectangle:
    """Representing a rectangle
    Attributes:
    number_of_instances(int): total rectangle instances
    print_symbol: used for string representation
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializing a new rectangle
        Arguments:
        width: integer width of the rectangle.
        height: integer height of the rectangle
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """get/set the width of the rectangle"""
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
        self.__height = value

    def area(self):
        """Return the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Recturn rectangle string object"""
        if self.__width == 0 or self.__height == 0:
            return ""
        ob_rectangle = []
        for j in range(self.__height):
            [ob_rectangle.append(str(self.print_symbol))
                for a in range(self.__width)]
            if j != self.__height - 1:
                ob_rectangle.append("\n")
        return ("".join(ob_rectangle))

    def __repr__(self):
        """Return the string representation"""
        str_rectangle = "Rectangle(" + str(self.__width)
        str_rectangle += ", " + str(self.__height) + ")"
        return (str_rectangle)

    def __del__(self):
        """print message for delete action of a rectangle"""
        print("Bye rectangle...")
