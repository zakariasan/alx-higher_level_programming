#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        allin = fct(*args)
    except Exception:
        print("Exception: {}".format(Exception), file=sys.stderr)
        return None
    else:
        return allin