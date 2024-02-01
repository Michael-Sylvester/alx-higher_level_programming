#!/usr/bin/python3
"""Python modual for add function"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Class holding unit tests for max integer function"""

    def test_positive_numbers(self):
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([2, 5, 9, 100]), 100)

    def test_one_number(self):
        self.assertEqual(max_integer([5]), 5)

    def test_multiple_max_number(self):
        self.assertEqual(max_integer([5, 2, 5, 3]), 5)

    def test_very_large_number(self):
        self.assertAlmostEqual(max_integer([50000000000000000000000, 2, 5, 3]), 50000000000000000000000)

    def test_long_list(self):
        self.assertEqual(max_integer([5, 2, 56, 3, 543, 3, 345, 34, 76, 765, 243, 23, 23, 54, 6, 5, 63]), 765)

    def test_negetive_numbers(self):
        self.assertEqual(max_integer([-2, -5, -9, -100]), -2)
        self.assertEqual(max_integer([-2, -5, 2, -100]), 2)

    def test_emptylist(self):
        self.assertEqual(max_integer([]), None)
    
    def test_no_argument(self):
        self.assertEqual(max_integer(), None)

    def test_int_and_floats(self):
        self.assertAlmostEqual(max_integer([1.1, 3, 55.5, 49]), 55.5)

    def test_small_floats(self):
        self.assertAlmostEqual(max_integer([0.44, 0.0004, 0.234, 0.465, -0.3534535, 0.8]), 0.8)

    def test_list_of_string_numbers(self):
        self.assertEqual(max_integer(["192834754"]), "192834754")

    def test_list_of_string_int_list(self):
        self.assertEqual(max_integer([["1"], ["9"], ["2"], ["8"]]), ["9"])
        self.assertEqual(max_integer(["33", "44", "98"]), "98")

    def test_list_of_string_list(self):
        self.assertEqual(
            max_integer([["hii"], ["ggs"], ["bbc"], ["sic"], ["ric"]]), ["sic"])

    def test_lists_of_lists_ofInt(self):
        self.assertEqual(max_integer([[4, 5, 6], [55, 33, 98]]), [55, 33, 98])

    def test_infinity(self):
        self.assertEqual(max_integer([464, float('inf'), float('-inf')]), float('inf'))

    def test_nan(self):
        self.assertEqual(max_integer([543, float('nan'), 433654]), 433654)

    def test_inputTypes(self):
        self.assertRaises(TypeError, max_integer, [{2, 4}, {55, 77}])

    def test_mixed_list(self):
        self.assertRaises(TypeError, max_integer,[44, 56, 756,"34"])

    def test_none(self):
        self.assertRaises(TypeError, max_integer, None)

    def test_dictionary(self):
        self.assertRaises(TypeError, max_integer, [{20: 23, 14: 45}, {"a": "b"}])

    def test_int(self):
        self.assertRaises(TypeError, max_integer, 33)