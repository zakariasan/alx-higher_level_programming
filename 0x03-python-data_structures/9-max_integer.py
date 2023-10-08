#!/usr/bin/python3

def max_integer(my_list=[]):
    if (len(my_list) == 0):
        return None
    maxi = my_list[0]
    for it in my_list:
        if (maxi < it):
            maxi = it
    return (maxi)
