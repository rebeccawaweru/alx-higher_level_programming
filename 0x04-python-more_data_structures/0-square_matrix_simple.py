#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_square = []
    for row in matrix:
        row_square = list(map(lambda x: x**2, row))
        matrix_square.append(row_square)
    return matrix_square
