#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    y = len(my_list)
    lst = my_list[:]

    if 0 <= idx < y:
        lst[idx] = element

    return(lst)
