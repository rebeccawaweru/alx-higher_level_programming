#!/usr/bin/python3

"""Define a new class MyList that inherits from list"""


class MyList(list):
    """Printing a sorted list"""

    def print_sorted(self):
        """print list in ascending order"""
        print(sorted(self))
