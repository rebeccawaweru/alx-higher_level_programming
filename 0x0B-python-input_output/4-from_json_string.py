#!/usr/bin/python3
"""Define function that returns an object represented by json string"""
import json


def from_json_string(my_str):
    """Return json string"""
    return json.loads(my_str)
