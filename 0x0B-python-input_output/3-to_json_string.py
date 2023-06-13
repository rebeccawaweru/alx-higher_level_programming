#!/usr/bin/python3
"""Define function to return JSON representation of an object(string)"""
import json


def to_json_string(my_obj):
    """Return JSON representation of the object"""
    return json.dumps(my_obj)
