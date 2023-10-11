#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map((lambda item: list(map(lambda item: item * item, item))),
                    matrix))
