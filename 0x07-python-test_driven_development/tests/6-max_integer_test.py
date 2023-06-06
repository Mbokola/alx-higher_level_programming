#!/usr/bin/python3
import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInt(unittest.TestCase):
    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([1, 2, 3, 4.6]), 4.6)
        self.assertEqual(max_integer([1, 2, 3, 4.6 + 1]), 5.6)
        self.assertEqual(max_integer([-1, -4, False, True]), True)
        self.assertEqual(max_integer([False, 0, -3, -4]), False)
        self.assertEqual(max_integer(["hi", "yes"]), "yes")
        self.assertEqual(max_integer([4, 4, 4, 4]), 4)
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([[1, 2], [3, 4]]), [3, 4])
        with self.assertRaises(TypeError):
            max_integer([3, "string"])
            max_integer([3, 4, [5, 6]])
