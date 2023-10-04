#!/usr/bin/python3
def remove_char_at(str, n):
    str1 = ''
    nb = 0
    for (i) in str:
        if nb != n:
            str1 += i
        nb = nb + 1
    return (str1)
