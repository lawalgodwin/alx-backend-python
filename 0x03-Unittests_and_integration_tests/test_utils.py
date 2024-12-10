#!/usr/bin/env python3
""" Parameterize a unit test """

import parameterized
from parameterized import parameterized
import unittest
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """ A test case for the nested_map function """

    @parameterized.expand([
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2)        
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ A method that tests for expected outputs """
        actual_result = access_nested_map(nested_map, path)
        self.assertEqual(actual_result, expected)


if __name__ == "__main__":
    unittest.main()