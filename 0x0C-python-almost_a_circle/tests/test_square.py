#!/usr/bin/python3
""" test_square module """
import unittest
from models.square import Square
from models.base import Base
from io import StringIO
import sys


class TestSquare(unittest.TestCase):
    """ TestSquare Class """
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_area(self):
        s1 = Square(5)
        self.assertEqual(s1.area(), 25)

    def test_size(self):
        s1 = Square(5)
        self.assertEqual(s1.size, 5)
        s1.size = 10
        self.assertEqual(s1.area(), 100)

    def test_str(self):
        s1 = Square(5)
        self.assertEqual(str(s1), '[Square] (1) 0/0 - 5')

    def test_validation(self):
        s1 = Square(5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s1.size = "9"
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s1.size = -4

    def test_update(self):
        s1 = Square(5)
        self.assertEqual(str(s1), '[Square] (1) 0/0 - 5')
        s1.update(10)
        self.assertEqual(str(s1), '[Square] (10) 0/0 - 5')
        s1.update(1, 2)
        self.assertEqual(str(s1), '[Square] (1) 0/0 - 2')
        s1.update(1, 2, 3)
        self.assertEqual(str(s1), '[Square] (1) 3/0 - 2')
        s1.update(1, 2, 3, 4)
        self.assertEqual(str(s1), '[Square] (1) 3/4 - 2')
        s1.update(x=12)
        self.assertEqual(str(s1), '[Square] (1) 12/4 - 2')
        s1.update(size=7, y=1)
        self.assertEqual(str(s1), '[Square] (1) 12/1 - 7')
        s1.update(size=7, id=89, y=1)
        self.assertEqual(str(s1), '[Square] (89) 12/1 - 7')

    def test_ro_dictionary(self):
        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        self.assertEqual(str(s1_dictionary), "{'id': 1, 'size': 10, 'x': 2,\
 'y': 1}")
        self.assertEqual(type(s1_dictionary), dict)
        s2 = Square(1, 1)
        s2.update(**s1_dictionary)
        self.assertEqual(str(s2), "[Square] (1) 2/1 - 10")
        self.assertFalse(s1 == s2)
