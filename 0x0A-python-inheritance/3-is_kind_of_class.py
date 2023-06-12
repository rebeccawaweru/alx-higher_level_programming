#!/usr/bin/python3

"""Define matching class and inheritance"""


def is_kind_of_class(obj, a_class):
    """Check if object is an instance or inheritance
    Arguments:
    obj: the object
    """
    if isinstance(obj, a_class):
        return True
    return False
