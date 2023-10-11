#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """Search and replace with new item"""
    txt_list = []
    for item in my_list:
        if (item == search):
            txt_list.append(replace)
        else:
            txt_list.append(item)
    return txt_list
