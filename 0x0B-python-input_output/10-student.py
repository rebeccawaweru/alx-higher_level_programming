#!/usr/bin/python3
"""Define a class Student"""


class Student():
    """Represent an instance of a student"""
    def __init__(self, first_name, last_name, age):
        """Initialize a new student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dictionary description with simple data structure"""
        if attrs is None:
            return self.__dict__
        else:
            dictionary = {}
            for a in attrs:
                if a in self.__dict__.keys():
                    dictionary[a] = self.__dict__[a]
            return dictionary
