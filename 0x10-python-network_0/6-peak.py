#!/usr/bin/python3
"""Function to find a peak"""
def find_peak(list_of_integers):
    """Function that finds a peak in a list of unsorted integers"""
    lst = list_of_integers
    y = len(lst)
    if y == 0:
        return
    x = y // 2
    if (x == y - 1 or lst[x] >= lst[x + 1]) and (x == 0 or lst[x] >= lst[x - 1]):
        return lst[x]
    if x != y - 1 and lst[x + 1] > lst[x]:
        return find_peak(lst[x + 1:])
    return find_peak(li[:m])
