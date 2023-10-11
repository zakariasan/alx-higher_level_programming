#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """sort a_dictionary."""
    kys = list(a_dictionary.keys())
    kys.sort()
    sorted_dic = {i: a_dictionary[i] for i in kys}
    for item in sorted_dic:
        print("{}: {}".format(item, sorted_dic[item]))
    return sorted_dic

print_sorted_dictionary = \
    __import__('6-print_sorted_dictionary').print_sorted_dictionary

a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low", 'ids': [1, 2, 3] }
new_dict = simple_delete(a_dictionary, 'track')
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)

print("--")
print("--")
new_dict = simple_delete(a_dictionary, 'c_is_fun')
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)

