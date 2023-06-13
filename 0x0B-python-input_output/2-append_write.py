#!/usr/bin/python3
"""Define function for appending a file"""


def append_write(filename="", text=""):
    """Append a text at the end of a file and return no of characters"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
