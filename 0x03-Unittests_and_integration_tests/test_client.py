#!/usr/bin/env python3
"""Test for Client.py module"""

import unittest
from unittest import TestCase
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(TestCase):
    """ A Test case for the GitHubOrgClient class """
    @parameterized.expand([
        ("goggle"),
        ("abc")
    ])
    @patch('client.get_json')
    def test_org(self, org, mock_get_json):
        """ A test for the org method """
        github_org_client = GithubOrgClient(org)
        ORG_URL = f"https://api.github.com/orgs/{org}"
        result1 = github_org_client.org()
        result2 = github_org_client.org()
        # Test that the get_json function is called only once
        mock_get_json.assert_called_once()
        # test that the call was made with the expected arg
        mock_get_json.assert_called_once_with(ORG_URL)
        # Test that the result of both first and second calls are the same
        self.assertEqual(result1, result2)


if __name__ == "__main__":
    unittest.main()
