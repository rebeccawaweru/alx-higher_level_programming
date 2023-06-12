#!/usr/bin/python3

"""Define class MyInt"""


class MyInt(int):
    """Rebel class"""

    def __eq__(self, number):
        """Return opposite of equals"""
        return super().__ne__(number)

    def __ne__(self, number):
        """Return opposite of not equal"""
        return super().__eq__(number)
