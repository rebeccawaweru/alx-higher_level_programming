#!/usr/bin/python3

"""Defines a function that adds attributes to objects"""


def add_attribute(obj, attribute, val):
    """Function to add attribute where possible
    Arguments:
    obj: the object
    attribute: the attribute
    val: the value
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, attribute, val)
    else:
        raise TypeError("can't add new attribute")
