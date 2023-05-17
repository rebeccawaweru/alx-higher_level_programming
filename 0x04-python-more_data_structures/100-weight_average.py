#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        average = 0
    else:
        x = sum(map(lambda x: x[0] * x[1], my_list))
        y = sum(map(lambda x: x[1], my_list))
        average = x / y
    return average
