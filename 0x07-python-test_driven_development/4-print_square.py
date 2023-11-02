#!/usr/bin/python3
""" function that prints a square with the character """


def print_square(size):
    """Print square if u have size"""
    if (not isinstance(size, int)):
        raise TypeError("size must be an integer")
    elif (size < 0):
        raise ValueError("size must be >= 0")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    else:
        for s in range(size):
            print('#' * size)
