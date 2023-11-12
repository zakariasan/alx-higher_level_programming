#!/usr/bin/python3
"""
Test : Unit test for square
"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """ test class """

    def setUp(self):
        """Create a default square for testing"""
        self.default_square = Square(5, 2, 3, 1)

    def test_attributes(self):
        """ test attr """
        self.assertEqual(self.default_square.size, 5)
        self.assertEqual(self.default_square.x, 2)
        self.assertEqual(self.default_square.y, 3)
        self.assertEqual(self.default_square.id, 1)

    def test_size_setter(self):
        """ test size setter """
        with self.assertRaises(ValueError):
            self.default_square.size = -5

        with self.assertRaises(TypeError):
            self.default_square.size = "string"

        self.default_square.size = 15
        self.assertEqual(self.default_square.size, 15)
        self.assertEqual(self.default_square.width, 15)
        self.assertEqual(self.default_square.height, 15)

    def test_str(self):
        """ str """
        expected_str = "[Square] (1) 2/3 - 5"
        self.assertEqual(str(self.default_square), expected_str)

    def test_update(self):
        """ update test """
        self.default_square.update(2, 8, 1, 5)
        self.assertEqual(self.default_square.id, 2)
        self.assertEqual(self.default_square.size, 8)
        self.assertEqual(self.default_square.x, 1)
        self.assertEqual(self.default_square.y, 5)

    def test_to_dictionary(self):
        """ test dic """
        expected_dict = {'id': 1, 'x': 2, 'size': 5, 'y': 3}
        self.assertEqual(self.default_square.to_dictionary(), expected_dict)
