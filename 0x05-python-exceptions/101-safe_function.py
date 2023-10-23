#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as expl:
        print("Exception: {}".format(expl), file=sys.stderr)
        return None
