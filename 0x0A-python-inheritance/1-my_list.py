#!/usr/bin/python3
"""Class from another class"""


class MyList(list):
    """ My class attr"""

    def __init__(self):
        super().__init__()

    def print_sorted(self):
        tmp = self.copy()
        tmp.sort()
        print(tmp)
