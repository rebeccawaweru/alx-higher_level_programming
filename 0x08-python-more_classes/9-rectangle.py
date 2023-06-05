#!/usr/bin/python3

"""Define a class Rectangle"""


class Rectangle:
    """Representing a rectangle
    Attributes:
    number_of_instances: total rectangle instances
    print_symbol: used for string representation
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializing a new reactangle
        Arguments:
        width: integer width of a rectangle
        height: integer height of a rectangle
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
        """get /set the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return rectangle with bigger area
        Arguments:
        rect_1: the first rectangle
        rect_2: the last rectangle
        Raises:
        TypeError: if either is not a rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Return new rectangle with equal size
        Arguments:
        size: the integer width and height of the new rectangle
        """
        return (cls(size, size))

    def __str__(self):
        """Return rectangle string object"""
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
        str_rectangle = "Rectangle(" + str(self._width)
        str_rectangle += ", " + str(self.__height) + ")"
        return (str_rectangle)

    def __del__(self):
        """print message for delete action of a rectangle"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
