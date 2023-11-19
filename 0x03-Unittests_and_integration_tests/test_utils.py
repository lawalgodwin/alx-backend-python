#!/usr/bin/env python3
"""Parameterize a unit test"""

from utils import access_nested_map
import unittest
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """Test for fuctions in the utils module"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, map, path, expected_output):
        """test for access_nested_map function"""
        real_out = access_nested_map(map, path)
        self.assertEqual(real_out, expected_output)


if __name__ == '__main__':
    unittest.main()
