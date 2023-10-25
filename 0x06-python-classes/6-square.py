#!/usr/bin/python3
"""Class of a square with size"""


class Square:
    """class content private size"""

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.position = position

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) != tuple or len(value) != 2 or type(value[0]) != int or\
                type(value[1]) != int or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0 ")
        else:
            self.__size = value

    def my_print(self):
        if not self.__size:
            print('')
        else:
            for x in range(0, self.__position[1]):
                print("")
            for x in range(0, self.__size):
                print(" " * self.__position[0], end='')
                print("#" * self.__size)
