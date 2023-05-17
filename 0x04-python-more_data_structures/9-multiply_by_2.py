#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary is not None:
        dictionary = dict(a_dictionary)
        for x, y in dictionary.items():
            dictionary[x] = y * 2
        return dictionary
