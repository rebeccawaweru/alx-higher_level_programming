#!/usr/bin/python3
"""Define function to create Object from JSON file"""


def load_from_json_file(filename):
    """Creating an object from JSON file"""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
