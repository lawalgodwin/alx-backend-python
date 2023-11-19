#!/usr/bin/env python3
"""Parameterize a unit test"""

from utils import access_nested_map, get_json
import unittest
from parameterized import parameterized
from unittest.mock import MagicMock, patch


class TestAccessNestedMap(unittest.TestCase):
    """Test for access_nested_map fuction in the utils module"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, map, path, expected_output):
        """test for access_nested_map function that it returs expected result
        """
        real_out = access_nested_map(map, path)
        self.assertEqual(real_out, expected_output)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, map, path):
        """tes for KEyError Exception in the access_nested_map function"""
        with self.assertRaises(KeyError):
            access_nested_map(map, path)


class TestGetJson(unittest.TestCase):
    """Test for the get_json function in the utils module"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_json_response):
        """test for get_json that it returns the expected result"""
        mock_response = MagicMock()
        mock_response.json.return_value = test_json_response
        with patch('requests.get') as mock_requests_get:
            mock_requests_get.return_value = mock_response
            real_response = get_json(test_url)
            self.assertEqual(real_response, test_json_response)


if __name__ == '__main__':
    unittest.main()
