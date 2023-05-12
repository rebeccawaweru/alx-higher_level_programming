#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    x = tuple_a[:2] + (0, 0)[:2 - len(tuple_a)]
    y = tuple_b[:2] + (0, 0)[:2 - len(tuple_b)]
    total = (x[0] + y[0], x[1] + y[1])
    return total
