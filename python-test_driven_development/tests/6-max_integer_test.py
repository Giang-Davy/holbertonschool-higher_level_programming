#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_max_at_the_end(self):
        self.assertEqual([1,2,3,4])4)
    def test_max_at_the_beginning(self):
        self.assertEqual([4,1,2,3])4)
    def test_max_in_the_middle(self):
        self.assertEqual([1,2,4,3])4)
    def test_one_negative_number_in_the_list(self):
        self.assertEqual([-1,2,3,4])4)
    def test_only_negative_numbers_in_the_list(self):
        self.assertEqual([-1,-2,-3,-4])-1)
    def test_list_of_one_element(self):
        self.assertEqual([1])1)
