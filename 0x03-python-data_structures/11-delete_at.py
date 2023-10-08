#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    if (idx >= len(my_list) or idx < 0):
        return my_list

    new_l = []
    for it in range(len(my_list)):
        if (it != idx):
            new_l.append(my_list[it])
    my_list = new_l
    return (my_list)
