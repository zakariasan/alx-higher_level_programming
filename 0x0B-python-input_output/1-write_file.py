#!/usr/bin/python3
"""
    function that writes a str to file (UTF8) and prints it to stdout:
"""


def write_file(filename="", text=""):
    """ writ file """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
