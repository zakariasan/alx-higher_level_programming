#!/usr/bin/python3
"""
    function insert txt in file
"""


def append_after(filename="", search_string="", new_string=""):
    """ insert txt to file """
    with open(filename, 'wr') as target:
        lines = target.readlines()
        for line in lines:
            target.write(line)
            if search_string in line:
                target.write(new_string + '\n')
