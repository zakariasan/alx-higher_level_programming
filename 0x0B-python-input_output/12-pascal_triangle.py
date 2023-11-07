#!/usr/bin/python3
"""
 pascal triangle
"""


def pascal_triangle(n):
    """ pascal triangle """
    if n <= 0:
        return []

    total = []
    for item in range(0, n):
        val = 1
        res = []
        for pr in range(0, item + 1):
            res.append(val)
            val = val * (item - pr) // (pr + 1)
        total.append(res)
    return total
