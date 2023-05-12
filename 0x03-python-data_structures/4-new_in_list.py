#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx not in range(len(my_list)):
        return mylist[:]
    lst = my_list[:]
    lst[idx] = element
    return lst
