#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    max_num = sorted(my_list, reverse=True)
    return max_num[0]
