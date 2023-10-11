#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    beg = [i for i, y in a_dictionary.items() if y == value]
    for item in beg:
        del a_dictionary[item]
    return a_dictionary
