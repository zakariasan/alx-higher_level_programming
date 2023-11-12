#!/usr/bin/python3
"""
Class : Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """desc of Square form Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """The width property."""
        return self.width

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        return "[{}] ({}) {}/{} - {}".format(type(self).__name__, self.id,
                                             self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """ Update attribute args and kwargs"""
        if len(args) == 0:
            for name, val in kwargs.items():
                self.__setattr__(name, val)
        else:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass

    def to_dictionary(self):
        """ to_dictionary funcc for square"""
        return {'id': getattr(self, 'id'), 'x': getattr(self, 'x'),
                'size': getattr(self, 'size'), 'y': getattr(self, 'y')}
