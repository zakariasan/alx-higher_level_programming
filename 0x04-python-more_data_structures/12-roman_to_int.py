#!/usr/bin/python3

def roman_to_int(roman_string):
    if (roman_string and type(roman_string) == str):
        res = 0
        prev = 0
        roman_dgt = {'I': 1, 'V': 5, 'X': 10, 'C': 100, 'L': 50, 'D': 500,
                     'M': 1000}
        for a in reversed(roman_string):
            val = roman_dgt[a]
            if (val < prev):
                res -= val
            else:
                res += val
            prev = val
        return res
    return 0
