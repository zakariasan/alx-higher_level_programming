#!/usr/bin/python3
"""Class of a Rectangle"""


class Rectangle:
    """class of Rectangle"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.height * self.width

    def perimeter(self):
        if (self.height == 0 or self.width == 0):
            return 0
        else:
            return 2 * (self.height + self.width)

    def __str__(self):
        if self.width and self.height:
            print = ''
            for _ in range(self.height):
                print += str(self.print_symbol) * self.width
                if _ < self.height - 1:
                    print += '\n'
            return print
        else:
            return ''

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
