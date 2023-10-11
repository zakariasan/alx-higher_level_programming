#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """sort a_dictionary."""
    kys = list(a_dictionary.keys())
    kys.sort()
    sorted_dic = {i: a_dictionary[i] for i in kys}
    for item in sorted_dic:
        print("{}: {}".format(item, sorted_dic[item]))
    return sorted_dic
