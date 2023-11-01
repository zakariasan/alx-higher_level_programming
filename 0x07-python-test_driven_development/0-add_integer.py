#!/usr/bin/python3
"""Function that add 2 integers"""


def add_integer(a, b=98):
    """Sum of tow nbrs"""
    if (not isinstance(a, (float, int))):
        raise TypeError("a must be an integer")
    elif (not isinstance(a, (float, int))):
        raise TypeError("b must be an integer")
    else:
        return (int(a) + int(b))
