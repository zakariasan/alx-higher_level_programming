#!/usr/bin/python3
"""BaseGeometry"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square of Rect """

    def __init__(self, size):
        self.__size = size
        Rectangle.__init__(self, self.__size, self.__size)

    def __str__(self):
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)

    def area(self):
        return self.__size * self.__size
