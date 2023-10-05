#!/usr/bin/python3
if __name__ == "__main__":
    import sys

if (len(sys.argv) - 1 != 0):
    print("{} arguments:".format(len(sys.argv) - 1))
    for item in range(1, len(sys.argv)):
        print("{:d}: {:s}".format(item, sys.argv[item]))
else:
    print("{} arguments.".format(len(sys.argv) - 1))
