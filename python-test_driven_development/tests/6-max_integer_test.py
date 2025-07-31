#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_normal_case(self):
        arr = [1, 2, 3, 6, 5, 9, 4]
        self.assertEqual(max_integer(arr), 9)
    def test_max_at_the_end(self):
        arr = [2, 4, 6, 8, 10, 12]
        self.assertEqual(max_integer(arr), 12)
    def test_negative_number(self):
        arr = [-1, -2, -3, -4, -5, -6]
        self.assertEqual(max_integer(arr), -1)
    def test_single_element(self):
        arr = [6]
        self.assertEqual(max_integer(arr), 6)
    def test_empty_list(self):
        arr = []
        self.assertEqual(max_integer(arr), None)
    def test_mixed_numbers(self):
        arr = [-1, -3, 6, -12, -76, 2]
        self.assertEqual(max_integer(arr), 6)
    def test_type_error(self):
        self.assertRaises(TypeError, max_integer, ["h", 1])
        self.assertRaises(TypeError, max_integer, [2, [2, 1]])

if __name__ == "__main__":
    unittest.main()