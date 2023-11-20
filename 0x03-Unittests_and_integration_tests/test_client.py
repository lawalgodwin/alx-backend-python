#!/usr/bin/env python3
"""Test for Client.py module"""
import unittest
from unittest.mock import patch, MagicMock, PropertyMock
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

    @parameterized.expand([
        ('google', {"repos_url": "https://api.someurl.com"})
        ])
    def test_public_repos_url(self, org_name, exp_repos_url: dict):
        """Mocking a property and unit-test the method ._public_repos_url
        Note: memoize automatically turns the decorated nethod into
        an instance property"""
        with patch.object(
            GithubOrgClient, 'org',
            new=exp_repos_url
        ):
            org_client = GithubOrgClient(org_name)
            real_repos_url = org_client._public_repos_url
            self.assertEqual(real_repos_url, exp_repos_url.get("repos_url"))


if __name__ == '__main__':
    unittest.main()
