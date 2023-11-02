#!/usr/bin/python3
"""Function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """func of matrix"""
    check = all(isinstance(ro, list) and len(ro) != 0 and
                all(isinstance(item, (int, float)) for item in ro) for ro in
                matrix)
    str = "Matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list) or not check:
        raise TypeError(str)

    if len(set(len(lst) for lst in matrix)) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    if (type(div) != int):
        if (type(div) != float):
            raise TypeError("div must be a number")
    if (not div):
        raise ZeroDivisionError("division by zero")
    return [[round(item / div, 2) for item in lst] for lst in matrix]
