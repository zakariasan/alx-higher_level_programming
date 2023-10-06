#!/usr/bin/python3
if __name__ == "__main__":
    from magic_calculation_102 import add, sub


def magic_calculation(a, b):
    if a < b:
        res = add(a, b)
        for i in range(4, 6):
            res = add(res, i)
        return res
    else:
        return sub(a, b)
