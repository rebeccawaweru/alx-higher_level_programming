#!/usr/bin/python3
"""Define function that returns dict description with simple data"""


def class_to_json(obj):
    """Function to return the dictionary description"""
    return obj.__dict__
