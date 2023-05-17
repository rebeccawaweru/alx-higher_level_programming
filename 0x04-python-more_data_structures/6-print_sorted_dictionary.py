#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys_sorted = sorted(a_dictionary.keys())
    for key in keys_sorted:
        val = a_dictionary[key]
        print(f"{key}: {val}")


if __name__ == '__main__':
    a_dictionary = {
            'language': "C",
            'Number:': 89,
            'track': "Low level",
            'ids': [1, 2, 3]
    }
    print_sorted_dictionary(a_dictionary)
