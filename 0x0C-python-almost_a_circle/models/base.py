#!/usr/bin/python3
"""Define a new class Base"""


class Base:
    """Representing class Base
    Attribute: __nb_objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializing a new instance of class Base
        Attribute:
        id - expected to be an integer
        __nb_objects
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
