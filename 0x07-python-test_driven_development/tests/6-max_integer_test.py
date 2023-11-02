#!/usr/bin/python3
"""Function for unitest"""

import unittest


class TestMaxInteger(unittest.TestCase):
    """Testing world with us"""

    def test_max(self):
        max_integer = __import__('6-max_integer').max_integer
        self.assertEqual(max_integer([1, 3, 5]), 5)
        self.assertEqual(max_integer([-1, -3, -5]), -1)
        self.assertEqual(max_integer([5, 0, 2]), 5)
        self.assertEqual(max_integer([-100, 5, 2]), 5)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([1, 2]), 2)
        self.assertEqual(max_integer([1, 12, 3, 4, 5, 5]), 12)
        self.assertEqual(max_integer([0, 0, 0, 0, 0, 0]), 0)
        self.assertEqual(max_integer([-1, 0, 0, 1, 1, 1]), 1)
        self.assertEqual(max_integer([-10, 10, 100, 210, 10001, 123]), 10001)
