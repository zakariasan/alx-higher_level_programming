#!/usr/bin/python3
"""BaseGeometry"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square of Rect """

    def __init__(self, size):
        Rectangle.__init__(self, size, size)
        self.__size
