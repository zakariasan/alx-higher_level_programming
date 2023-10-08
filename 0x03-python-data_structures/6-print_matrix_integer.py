#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for item in matrix:
        for row in item:
            if (item.index(row) != 0):
                print(" ", end='')
            print("{:d}".format(row), end='')
        print()
