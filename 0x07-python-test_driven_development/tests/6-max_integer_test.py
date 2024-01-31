#!/usr/bin/python3
"""Python modual for add function"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Class holding unit tests for max integer function"""

    def test_positive_numbers(self):
        self.assertAlmostEqual(max_integer([]), None)
        self.assertAlmostEqual(max_integer([2, 5, 9, 100]), 100)
        self.assertAlmostEqual(max_integer([5]), 5)

    def test_negetive_numbers(self):
        self.assertAlmostEqual(max_integer([-2, -5, -9, -100]), -2)
        self.assertAlmostEqual(max_integer([-2, -5, 2, -100]), 2)

    def test_emptylist(self):
        self.assertAlmostEqual(max_integer([]), None)

    def test_inputTypes(self):
        self.assertRaises(TypeError, max_integer, "gg")
        self.assertRaises(TypeError, max_integer, [[4, 5, 6], [55, 33, 98]])
        self.assertRaises(TypeError, max_integer, [{2, 4}, {55, 77}])
        self.assertRaises(TypeError, max_integer, ["33", "44", "98"])
        self.assertRaises(TypeError, max_integer, [1.1, 3.55, 55.5])
