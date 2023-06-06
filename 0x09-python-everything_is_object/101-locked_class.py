#!/usr/bin/python3

""""Define a class LockedClass"""


class LockedClass:
    """Prevent user from creating new instance attributes
    except for first_name
    """
    __slots__ = ['first_name']
