#!/usr/bin/env python3
""" Parameterize a unit test """

import parameterized
from parameterized import parameterized
import unittest
from unittest.mock import patch, MagicMock, Mock
from utils import access_nested_map, get_json, memoize
import utils


class TestAccessNestedMap(unittest.TestCase):
    """ A test case for the util, client and fixtures modules  """

    @parameterized.expand([
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ A method that tests for expected outputs """
        actual_result = access_nested_map(nested_map, path)
        self.assertEqual(actual_result, expected)

    @parameterized.expand([
        ({}, ("a",), ),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """ Test for exception(KeyError) """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """ Mock HTTP calls """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url, payload):
        """ Test for the get_json function """
        with patch.object(utils.requests, "get") as mock_requests_get:
            # set the return value of the .json() method on the response object
            mock_requests_get.return_value.json.return_value = payload
            actual = get_json(url)
            expected = payload
            # Test that the get method was called only once per input test_url
            mock_requests_get.assert_called_once_with(url)
            # Test that the output of get_json is equal to test_payload
            self.assertDictEqual(actual, expected)


class TestMemoize(unittest.TestCase):
    """ Test for memoization method """
    def test_memoize(self):
        """ Test that when calling a_property twice, the correct result is
        returned but a_method is only called once
        """
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(TestClass, "a_method") as mock_a_method:
            myclass = TestClass()
            result1 = myclass.a_property()
            result2 = myclass.a_property()
            # Test that the a_method was called only once due to memoization
            mock_a_method.assert_called_once()
            self.assertEqual(result1, result2)


if __name__ == "__main__":
    unittest.main()
