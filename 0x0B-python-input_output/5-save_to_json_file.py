#!/usr/bin/python3
"""Define function to save object to a file using json"""


def save_to_json_file(my_obj, filename):
    """Save json to a file using JSON"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
