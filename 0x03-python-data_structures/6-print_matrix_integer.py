#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for item in matrix:
        for row in item:
            print("{}".format(row), end='')
            if (item.index(row) != len(item) - 1):
                print(" ", end='')
        print()
    return matrix
