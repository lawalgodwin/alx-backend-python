#!/usr/bin/env python3
"""Test for Client.py module"""
import unittest
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test for the GithubOrgClient class"""

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, org_name: str, mock_get_json: MagicMock):
        """test that the GithubOrgClient.org returns the correct value """
        spec = GithubOrgClient(org_name)
        org_url = 'https://api.github.com/orgs/{}'.format(org_name)
        spec.org()
        mock_get_json.assert_called_once_with(org_url)


if __name__ == '__main__':
    unittest.main()
