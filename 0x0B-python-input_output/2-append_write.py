#!/usr/bin/python3
"""
    function that append a str to file (UTF8) and prints it to stdout:
"""


def append_write(filename="", text=""):
    """ append file """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
