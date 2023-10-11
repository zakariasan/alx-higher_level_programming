#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    return {key: val for key, val in a_dictionary.item() if val != value}
