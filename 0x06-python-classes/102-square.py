#!/usr/bin/python3
"""Class of a square with size"""


class Square:
    """class content private size"""

    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0 ")
        else:
            self.__size = size

    def area(self):
        return self.__size * self.__size

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

    def __lt__(self, second):
        return self.area() < second.area()

    def __le__(self, second):
        return self.area() <= second.area()

    def __eq__(self, second):
        return self.area() == second.area()

    def __ne__(self, second):
        return self.area() != second.area()

    def __gt__(self, second):
        return self.area() > second.area()

    def __ge__(self, second):
        return self.area() >= second.area()
