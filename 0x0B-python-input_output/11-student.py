#!/usr/bin/python3
"""
 class Student
"""


class Student:
    """ class pt json """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        out = {}
        if attrs is not None:
            for att in attrs:
                if hasattr(self, att):
                    out[att] = getattr(self, att)
            return out
        return self.__dict__

    def reload_from_json(self, json):
        for name, value in json.items():
            setattr(self, name, value)
