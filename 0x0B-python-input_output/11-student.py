#!/usr/bin/python3
"""Define a class Student"""


class Student:
    """Representing a Student"""
    def __init__(self, first_name, last_name, age):
        """Initializing a new instance of class Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves dictionary representation of a Student"""
        if attrs is None:
            return self.__dict__
        else:
            dictionary = []
            for a in attrs:
                if a in self.__dict__.keys():
                    dictionary[a] = self.__dict__[a]
            return dictionary

    def reload_from_json(self, json):
        """Replaces all attributes of instance"""
        for a, b in json.items():
            setattr(self, a, b)
