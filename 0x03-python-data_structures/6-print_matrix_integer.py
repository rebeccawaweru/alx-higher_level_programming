#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in range(len(matrix)):
        for x in range(len(matrix[row])):
            if x != 0:
                print(" ", end='')
            print("{:d}".format(matrix[row][x]), end='')
        print()
