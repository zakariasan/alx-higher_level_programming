#!/usr/bin/python3
"""
Write a script that adds all arguments to a Python list
"""
import sys
save_from_json = __import__('5-save_to_json_file').save_to_json_file
load_from_json = __import__('6-load_from_json_file').load_from_json_file


def load_add_save(ar, filename):
    """ JSON from file to obj """

    try:
        lst = load_from_json(filename)
    except FileNotFoundError:
        lst = []
    lst.extend(ar)
    save_from_json(lst, filename)


if __name__ == '__main__':
    load_add_save(sys.argv[1:], "add_item.json")
