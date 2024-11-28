#!/usr/bin/python3
"""Module to test the max_integer function.

This module contains tests for the function `max_integer`, which
returns the maximum integer from a list of integers. If the list is empty,
it returns None.
"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_max_at_the_end(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_the_beginning(self):
        self.assertEqual(max_integer([4, 1, 2, 3]), 4)

    def test_max_in_the_middle(self):
        self.assertEqual(max_integer([1, 2, 4, 3]), 4)

    def test_one_negative_number_in_the_list(self):
        self.assertEqual(max_integer([-1, 2, 3, 4]), 4)

    def test_only_negative_numbers_in_the_list(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_list_of_one_element(self):
        self.assertEqual(max_integer([1]), 1)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

if __name__ == '__main__':
    unittest.main()
