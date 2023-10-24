#!/usr/bin/python3
"""Class of a square with size"""


class Square:
    """class content private size"""

    def __init__(self, size=0):
        if type(size) == int and size >= 0:
            self.__size = size
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
