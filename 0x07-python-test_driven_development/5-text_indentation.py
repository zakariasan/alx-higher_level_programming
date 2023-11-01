#!/usr/bin/python3
""" function that prints a square with the character .and ?"""


def text_indentation(text):
    if (not isinstance(text, str)):
        raise TypeError("text must be a string")
    ch = 0
    while (ch < len(text)):
        print("{}".format(text[ch]), end='')
        if (text[ch] == '.' or text[ch] == '?' or text[ch] == ':'):
            print("\n")
            ch += 1
            while ch < len(text) and text[ch] in ' \t\v\r':
                ch += 1
        else:
            ch += 1
