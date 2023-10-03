#!/usr/bin/python3
for d in range(0, 8):
    for v in range(0, 10):
        if (d < v):
            print("{:d}{:d}".format(d, v), end=", ")
print("{:d}{:d}".format(d + 1, v))
