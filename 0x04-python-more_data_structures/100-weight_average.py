#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        average = 0
    x = sum(map(lambda x: x[0] * x[1], my_list))
    y = sum(map(lambda x: x[1], my_list))
    average = x / y
    return average
