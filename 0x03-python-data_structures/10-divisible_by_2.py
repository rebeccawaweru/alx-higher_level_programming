#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    final_list = []
    for x in my_list:
        final_list.append(x % 2 == 0)
    return final_list
