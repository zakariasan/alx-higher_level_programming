#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    a_dictionary = {key: val for key, val in a_dictionary.item() if val !=
                    value}
    return a_dictionary
