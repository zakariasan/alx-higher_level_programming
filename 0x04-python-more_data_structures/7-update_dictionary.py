#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """Update a_dictionary."""
    if key in a_dictionary.keys():
        for it in a_dictionary:
            if (it == key):
                a_dictionary[it] = value
    else:
        a_dictionary[key] = value
    return (a_dictionary)
