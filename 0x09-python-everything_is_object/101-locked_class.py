#!/usr/bin/python3
"""Class lockked """


class LockedClass:
    "prevent from creating other"
    __slots__ = ('first_name', )
