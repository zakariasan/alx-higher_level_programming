#!/usr/bin/python3

def uniq_add(my_list=[]):
    """Be unique in the list"""
    res = 0
    for item in set(my_list):
        res += item
    return res
