#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """ Map over a matrix and return new world matrix"""
    tmp_matrix = []
    for item in matrix:
        tmp_matrix.append(list(map(lambda x: x*x, item)))
    return tmp_matrix
