#!/usr/bin/python3
import math


class MagicClass:

    """ hello class of MagicClass
    that can do better"""
    def __init__(self, radius):
        if not (isinstance(radius, int) or isinstance(radius, float)):
            raise TypeError('radius must be a number')
        self.__radius = radius

    """try the best"""
    def area(self):
        return self.__radius ** 2 * math.pi

    """try the best"""
    def circumference(self):
        return 2 * math.pi * self.__radius
