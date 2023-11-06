#!/usr/bin/python3
"""  function that returns True if the object is an instance of, or if the i
object is an instance of a class that inherited from, the specified class ;
otherwise False."""


def is_kind_of_class(obj, a_class):
    """ Return True if its a Obj"""
    if isinstance(obj, a_class):
        return True
    return issubclass(a_class, type(obj))
