#!/usr/bin/python3
"""Define function that inserts a line of text to a file"""


def append_after(filename="", search_string="", new_string=""):
    """Append string with a new string"""
    with open(filename, "r+", encoding="utf-8") as f:
        text = ""
        for n in f:
            text += n
            if search_string in n:
                text += new_string
        f.seek(0)
        f.write(text)
