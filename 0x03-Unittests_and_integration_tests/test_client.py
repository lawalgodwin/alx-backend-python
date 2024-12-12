#!/usr/bin/env python3
"""Test for Client.py module"""

import unittest
from unittest import TestCase
from unittest.mock import patch, PropertyMock
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

    @parameterized.expand([
        ("goggle", {"repos_url": "https://api.someurl.com"}),
        ("abc", {"repos_url": "https://api.anotherurl.com"})
    ])    
    def test_public_repos_url(self, org, expected_repos_url):
        """ A unit test for GithubOrgClient._public_repos_url """
        with patch.object(GithubOrgClient, 'org', new_callable=PropertyMock) as mock_org:
            mock_org.return_value = expected_repos_url
            github_org_client = GithubOrgClient(org)
            actual_repos_url = github_org_client._public_repos_url
            self.assertEqual(actual_repos_url, expected_repos_url.get("repos_url"))


if __name__ == "__main__":
    unittest.main()
