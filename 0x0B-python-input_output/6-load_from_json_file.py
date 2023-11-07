#!/usr/bin/python3
"""
    function that load and write JSON object to file
"""
import json


def load_from_json_file(filename):
    """ JSON from file to obj """
    with open(filename, 'r') as target:
        return json.loads(target.read())
