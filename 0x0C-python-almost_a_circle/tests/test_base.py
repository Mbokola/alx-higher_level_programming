#!/usr/bin/python3
""" test_base """
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """ TestBase class """
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_instances(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)
        b4 = Base(12)
        self.assertEqual(b4.id, 12)
        b5 = Base()
        self.assertEqual(b5.id, 4)

    def test_json_string_to_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), '[{"id": 1, "width": 10,\
 "height": 7, "x": 2, "y": 8}, {"id": 2, "width": 2, \
"height": 4, "x": 0, "y": 0}]')
