#!/usr/bin/python3
"""Define function that returns lists of integers"""


def pascal_triangle(n):
    """Return a list of lists of integers representing triangle"""
    if n <= 0:
        return []
    if n == 1:
        return [[1]]

    tri = [[1]]
    for rows in range(n-1):
        tri.append([x+y for x, y in zip([0] + tri[-1], tri[-1] + [0])])
    return tri
