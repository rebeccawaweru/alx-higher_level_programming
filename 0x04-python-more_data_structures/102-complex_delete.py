#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value:
        for key in list(a_dictionary.keys()):
            if value == a_dictionary[key]:
                del a_dictionary[key]
    return a_dictionary
