#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    new_t = []
    for item in range(0, len(my_list)):
        new_t.append(my_list[item] % 2 == 0)
    return (new_t)
