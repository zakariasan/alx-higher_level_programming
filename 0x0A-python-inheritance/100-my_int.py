#!/usr/bin/python3
"""Classic int"""


class MyInt(int):
    """ try int in my logic """

    def __eq__(self, nbr):
        return self.real != nbr

    def __ne__(self, nbr):
        return self.real == nbr
