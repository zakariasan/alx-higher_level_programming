#!/usr/bin/python3
"""
Class : Unit test for Base
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os


class TestBase(unittest.TestCase):
    """ Test Base """

    def test_init(self):
        """init test"""
        b1 = Base()
        self.assertEqual(b1.id, 5)

        b2 = Base()
        self.assertEqual(b2.id, 6)

        b3 = Base(100)
        self.assertEqual(b3.id, 100)

    def test_to_json_string(self):
        """ to json str test"""

        r1 = Rectangle(10, 7, 2, 8)
        r1_dict = r1.to_dictionary()
        result = Base.to_json_string([r1_dict])
        self.assertIsInstance(result, str)

    def test_save_to_file(self):
        """ save t file test"""

        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(5, 5)
        Rectangle.save_to_file([r1, r2])
        self.assertTrue(os.path.isfile("Rectangle.json"))

        s1 = Square(5)
        s2 = Square(10, 2, 1)
        Square.save_to_file([s1, s2])
        self.assertTrue(os.path.isfile("Square.json"))

    def test_from_json_string(self):
        """ test from json str """

        json_string = '[{"id": 1, "width": 2, "height": 3, "x": 4, "y": 5}]'
        result = Base.from_json_string(json_string)
        self.assertIsInstance(result, list)

    def test_create(self):
        """ test  create """

        r1 = Rectangle(10, 7, 2, 8)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertEqual(r1.id, r2.id)

        s1 = Square(5)
        s1_dict = s1.to_dictionary()
        s2 = Square.create(**s1_dict)
        self.assertEqual(s1.id, s2.id)

    def test_load_from_file(self):
        """ test load from """

        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(5, 5)
        Rectangle.save_to_file([r1, r2])
        rectangles = Rectangle.load_from_file()
        self.assertIsInstance(rectangles, list)
        self.assertEqual(len(rectangles), 2)

        s1 = Square(5)
        s2 = Square(10, 2, 1)
        Square.save_to_file([s1, s2])
        squares = Square.load_from_file()
        self.assertIsInstance(squares, list)
        self.assertEqual(len(squares), 2)
