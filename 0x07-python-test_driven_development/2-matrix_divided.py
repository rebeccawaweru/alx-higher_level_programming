#!/usr/bin/python3

""" matrix_divided
Divides all elements of a matrix by given divisor
Matrix should be a list
Other types raise TypeError
"""


def matrix_divided(matrix, div):
    """ matrix_divided
    Divides all elements of a matrix by a given divisor

    Args:
    matrix (list): A matrix represented as a list of
    lists of integers or floats.
    div: the divisor should be integer or float

    Returns:
    list: A new matric with all elements divided by div

    Raises:
    TypeError: If the matrix is not a list of lists of integers
    or floats, div is not a number or each row is not the same size
    ZeroDivisionError: when div is 0
    """
    if not isinstance(matrix, list) or any(not
       isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")
    row_sizes = [len(row) for row in matrix]
    if len(set(row_sizes)) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    fresh_matrix = []
    for row in matrix:
        fresh_row = [round(element / div, 2) for element in row]
        fresh_matrix.append(fresh_row)
    return fresh_matrix
