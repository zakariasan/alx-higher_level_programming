#!/usr/bin/python3
"""Class of a square with size"""


class Square:
    """class content private size"""

    def __init__(self, size=0):
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if not self.__size:
            print('')
        for x in range(0, self.__size):
            print("#" * self.__size)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0 ")
        else:
            self.__size = value
