#!/usr/bin/python3

"""Define an inherited class matching function"""


def inherits_from(obj, a_class):
    """Checking if an object is inherited
    Arguments:
    obj: the object
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
