#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list):
        up = 0
        down = 0
        for gr in my_list:
            up += (gr[0] * gr[1])
            down += (gr[1])
        return (up/down)
    return (0)
