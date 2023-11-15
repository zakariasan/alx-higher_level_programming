#!/usr/bin/python3
"""
Test : Unit test for rectangle
"""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """ test of class rectangle """

    def setUp(self):
        """ Create a default rectangle for testing """
        self.default_rectangle = Rectangle(10, 5, 2, 3, 1)
        self.r1 = Rectangle(1, 13)
        self.assertEqual(self.r1.width, 1)
        self.r2 = Rectangle(1, 13, 23)
        self.assertEqual(self.r2.height, 13)
        self.r3 = Rectangle(1, 13, 23, 3, 100)
        self.assertEqual(self.r3.id, 100)
        self.assertIsInstance(Rectangle(11, 11), Base)

    def test_attributes(self):
        """ play with attr """

        self.assertEqual(self.default_rectangle.width, 10)
        self.assertEqual(self.default_rectangle.height, 5)
        self.assertEqual(self.default_rectangle.x, 2)
        self.assertEqual(self.default_rectangle.y, 3)
        self.assertEqual(self.default_rectangle.id, 1)

    def test_width_setter(self):
        """ with setter test """
        with self.assertRaises(TypeError) as t:
            self.r1 = Rectangle("1", 100)

        self.assertEqual(str(t.exception), "width must be an integer")
        with self.assertRaises(TypeError):
            self.r1.width = "width must be an integer"

        with self.assertRaises(TypeError):
            self.r2 = Rectangle(1, "1")

        with self.assertRaises(TypeError):
            self.r2.height = "height must be an integer"

        with self.assertRaises(TypeError):
            self.r1 = Rectangle(1, 2, "3")

        with self.assertRaises(TypeError):
            self.r1.x = "x must be an integer"

        with self.assertRaises(TypeError):
            self.r1 = Rectangle(1, 2, 3, "4")

        with self.assertRaises(TypeError):
            self.r1.y = "y must be an integer"

        with self.assertRaises(ValueError):
            self.default_rectangle.width = 0

        with self.assertRaises(TypeError):
            self.default_rectangle.width = "width must be > 0"

        with self.assertRaises(ValueError):
            self.r1.width = 0

        with self.assertRaises(TypeError):
            self.r1.width = "width must be > 0"

        with self.assertRaises(ValueError):
            self.default_rectangle.width = -5

        with self.assertRaises(TypeError):
            self.default_rectangle.width = "width must be an integer"

        self.default_rectangle.width = 15
        self.assertEqual(self.default_rectangle.width, 15)

    def test_height_setter(self):
        """ hight setter test """
        with self.assertRaises(ValueError):
            self.default_rectangle.height = -5

        with self.assertRaises(ValueError):
            self.r1.height = -5

        with self.assertRaises(TypeError):
            self.r1.height = "height must be an integer"

        with self.assertRaises(TypeError):
            self.default_rectangle.height = "height must be an integer"

        self.default_rectangle.height = 15
        self.assertEqual(self.default_rectangle.height, 15)

    def test_x_setter(self):
        """ x setter test """
        with self.assertRaises(ValueError):
            self.default_rectangle.x = -5

        with self.assertRaises(TypeError):
            self.default_rectangle.x = "x must be >= 0"

        self.default_rectangle.x = 15
        self.assertEqual(self.default_rectangle.x, 15)

    def test_y_setter(self):
        """ y setter test """
        with self.assertRaises(ValueError):
            self.default_rectangle.y = -5

        with self.assertRaises(TypeError):
            self.default_rectangle.y = "y must be >= 0"

        self.default_rectangle.y = 15
        self.assertEqual(self.default_rectangle.y, 15)

    def test_area(self):
        """ area test """
        self.assertEqual(self.default_rectangle.area(), 10 * 5)

    def test_display(self):
        """  Redirect stdout to capture printed output """
        import sys
        from io import StringIO
        original_stdout = sys.stdout
        sys.stdout = StringIO()

        self.default_rectangle.display()
        output = sys.stdout.getvalue()
        expected_output = "\n" * 3 + "  ##########\n" * 5

        self.assertEqual(output, expected_output)

        # Reset redirect.
        sys.stdout = original_stdout

    def test_to_dictionary(self):
        """ dic test """
        expected_dict = {'x': 2, 'y': 3, 'id': 1, 'height': 5, 'width': 10}
        self.assertEqual(self.default_rectangle.to_dictionary(), expected_dict)

    def test_update(self):
        """ test update """
        self.default_rectangle.update(2, 8, 4, 1, 5)
        self.assertEqual(self.default_rectangle.id, 2)
        self.assertEqual(self.default_rectangle.width, 8)
        self.assertEqual(self.default_rectangle.height, 4)
        self.assertEqual(self.default_rectangle.x, 1)
        self.assertEqual(self.default_rectangle.y, 5)
