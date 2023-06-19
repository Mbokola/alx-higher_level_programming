#!/usr/bin/python3
""" test_rectangle module """
import unittest
from models.rectangle import Rectangle
from models.base import Base
from io import StringIO
import sys


class TestRectangle(unittest.TestCase):
    """ Unittests for Rectangle Class """
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_id(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_validation(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, "2")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(10, 2)
            r.x = {}
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(10, 2)
            r.width = -10
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(10, 2, 3, -1)

    def test_area(self):
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    def test_dispaly(self):
        r1 = Rectangle(4, 6)
        expected = "####\n####\n####\n####\n####\n####\n---\n##\n##\n"

        captured_output = StringIO()
        sys.stdout = captured_output

        r1.display()
        print("---")
        r1 = Rectangle(2, 2)
        r1.display()
        output = captured_output.getvalue()
        self.assertEqual(output, expected)
        sys.stdout = sys.__stdout__

    def test_display1(self):
        expected = "\n\n  ##\n  ##\n  ##\n---\n ###\n ###\n"
        r1 = Rectangle(2, 3, 2, 2)

        captured_output = StringIO()
        sys.stdout = captured_output

        r1.display()
        print("---")
        r2 = Rectangle(3, 2, 1, 0)
        r2.display()
        output = captured_output.getvalue()
        self.assertEqual(output, expected)
        sys.stdout = sys.__stdout__

    def test_str(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        r2 = Rectangle(5, 5, 1)
        expected = "[Rectangle] (12) 2/1 - 4/6\n[Rectangle] (1) 1/0 - 5/5\n"

        captured_output = StringIO()
        sys.stdout = captured_output
        print(r1)
        print(r2)
        output = captured_output.getvalue()
        self.assertEqual(output, expected)
        sys.stdout = sys.__stdout__

    def test_update(self):
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/10")
        r1.update(89)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 10/10")
        r1.update(89, 2)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/10")
        r1.update(89, 2, 3)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/3")
        r1.update(89, 2, 3, 4)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/10 - 2/3")
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/5 - 2/3")

    def test_update1(self):
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/10")
        r1.update(height=1)
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/1")
        r1.update(width=1, x=2)
        self.assertEqual(str(r1), "[Rectangle] (1) 2/10 - 1/1")
        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r1), "[Rectangle] (89) 3/1 - 2/1")
        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r1), "[Rectangle] (89) 1/3 - 4/2")

    def test_ro_dictionary(self):
        r1 = Rectangle(10, 2, 1, 9)
        self.assertEqual(str(r1), "[Rectangle] (1) 1/9 - 10/2")
        r1_dictionary = r1.to_dictionary()
        self.assertEqual(str(r1_dictionary), "{'id': 1, 'width': 10, \
'height': 2, 'x': 1, 'y': 9}")
        self.assertEqual(type(r1_dictionary), dict)
        r2 = Rectangle(1, 1)
        self.assertEqual(str(r2), "[Rectangle] (2) 0/0 - 1/1")
        r2.update(**r1_dictionary)
        self.assertEqual(str(r2), "[Rectangle] (1) 1/9 - 10/2")
        self.assertFalse(r1 == r2)
