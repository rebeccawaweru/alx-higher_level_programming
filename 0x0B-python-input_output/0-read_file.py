#!/usr/bin/python3
"""Define function for reading file"""


def read_file(filename=""):
    """Print contents of file to stdout"""
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")
