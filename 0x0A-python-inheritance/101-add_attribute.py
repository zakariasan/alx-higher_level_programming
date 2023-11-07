#!/usr/bin/python3
"""func st attr"""


def add_attribute(obj, attribute, res):
    """add new att if not exit"""

    if (hasattr(obj, "__dict__")):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, res)
