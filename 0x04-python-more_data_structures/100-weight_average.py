#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list and len(my_list) > 0:
        up = 0
        down = 0
        for gr in my_list:
            up += (gr[0] * gr[1])
            down += (gr[1])
            return (up/down)
    return (0)
