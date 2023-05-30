#!/usr/bin/python3

"""Define MagicClass that matches the bytecode provided"""

import math


class MagicClass:
    """Repping a circle"""

    def __init__(self, c=0):
        """New Magic class
        Arg:
        c : radius of the circle. Should be float and int
        """
        self.__c = 0
        if not isinstance(c, int) and not isinstance(c, float):
            raise TypeError("radius must be a number")
        self.__c = c

    def area(self):
        """Return area of magic class"""
        return (self.__c ** 2 * math.pi)

    def circlecircumference(self):
        """Return circumference of circle"""
        return (math.pi * 2 * self._c)
