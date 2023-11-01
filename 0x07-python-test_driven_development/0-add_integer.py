#!/usr/bin/python3
"""Function that add 2 integers"""


def add_integer(a, b=98):
    if (type(a) != int):
        if (type(a) != float):
            raise TypeError("a must be an integer")

    if (type(b) != int):
        if (type(b) != float):
            raise TypeError("b must be an integer")

    return (int(a) + int(b))
