#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        keys = a_dictionary.keys()
        return max(keys, key=lambda key: a_dictionary[key])
