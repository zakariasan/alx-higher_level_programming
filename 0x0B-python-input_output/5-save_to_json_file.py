#!/usr/bin/python3
"""
    function that write JSON object to file
"""
import json


def save_to_json_file(my_obj, filename):
    """ JSON file to file """
    with open(filename, 'w') as target:
        json.dump(my_obj, target)
