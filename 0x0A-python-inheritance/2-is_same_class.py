#!/usr/bin/python3

"""Function to check matching class"""


def is_same_class(obj, a_class):
    """Inspecting if an object is same as
    instance of a given class
    Arguments:
    obj: the object to check
    """
    if type(obj) == a_class:
        return True
    return False
