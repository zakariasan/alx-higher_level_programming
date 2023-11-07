#!/usr/bin/python3
"""
    function that returns an JSON object
"""
import json


def from_json_string(my_str):
    """ JSON file to str """
    return json.loads(my_str)
