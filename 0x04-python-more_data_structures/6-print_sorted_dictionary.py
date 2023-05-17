#!/usr/bin/pyhon3
def print_sorted_dictionary(a_dictionary):
    keys_sorted = sorted(a_dictionary.keys())
    for key in keys_sorted:
        val = a_dictionary[key]
        print("{}: {}".format(key, val))
