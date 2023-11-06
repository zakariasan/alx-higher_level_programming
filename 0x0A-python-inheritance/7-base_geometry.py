#!/usr/bin/python3
"""BaseGeometry"""


class BaseGeometry:
    """BaseGeometry (class)
        attr:
            area(): raise Exception
            integer_validator: check name value
    """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate value and namee"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
