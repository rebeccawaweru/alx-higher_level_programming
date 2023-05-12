#!/usr/bin/python3
def no_c(my_string):
    final_string = ""
    for s in my_string:
        if s not in ('c', 'C'):
            final_string += s
    return final_string
