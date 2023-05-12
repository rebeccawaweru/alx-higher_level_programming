#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for x, num in enumerate(row):
            print("{}".format(num), end="")
            if x < len(row) - 1:
                print(" ", end="")
        print()
