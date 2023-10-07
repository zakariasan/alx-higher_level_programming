#!/usr/bin/python3

def no_c(my_string):
    str = ''
    for item in my_string:
        if (item != 'c' and item != 'C'):
            str += item
        my_string = str
    return my_string
