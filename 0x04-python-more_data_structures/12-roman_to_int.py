#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if type(roman_string) is not str or roman_string is None:
        return 0
    x = 0
    prev_value = 0
    for s in roman_string:
        if s not in roman:
            return 0
        val = roman[s]
        if val > prev_value:
            x += val - 2 * prev_value
        else:
            x += val
        prev_value = val
    return x
