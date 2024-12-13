#!/usr/bin/env python3
"""Test for Client.py module"""

import unittest
from unittest import TestCase
from unittest.mock import patch, PropertyMock, MagicMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


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
        with patch.object(
            GithubOrgClient, 'org',
            new_callable=PropertyMock
        ) as mock_org:
            mock_org.return_value = expected_repos_url
            github_org_client = GithubOrgClient(org)
            actual_repos_url = github_org_client._public_repos_url
            self.assertEqual(
                actual_repos_url,
                expected_repos_url.get("repos_url")
            )

    @patch('client.get_json')
    def test_public_repos(self, mock_json: MagicMock):
        """ A unit test for the GithubOrgClient.public_repos """
        mock_json.return_value = [{"name": "goggle"}, {"name": "abc"}]
        with patch.object(
            GithubOrgClient, "_public_repos_url",
            new_callable=PropertyMock,
            return_value="Some generic public repos url"
        ) as mock_public_repos_url:

            github_org_client = GithubOrgClient("test_org_name")

            actual = github_org_client.public_repos()
            mock_json.assert_called_once()
            mock_public_repos_url.assert_called_once()
            expected = ["goggle", "abc"]
            self.assertEqual(actual, expected)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """ A unit test for the GithubOrgClient.has_license """
        has_licence = GithubOrgClient.has_license(repo, license_key)
        self.assertIs(has_licence, expected)


@parameterized_class([
    {
        "org_payload": TEST_PAYLOAD[0][0],
        "repos_payload": TEST_PAYLOAD[0][1],
        "expected_repos": TEST_PAYLOAD[0][2],
        "apache2_repos": TEST_PAYLOAD[0][3]
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Integration Test for GithubOrgClient.public_repos method  """

    @classmethod
    def setUpClass(cls):
        """ start a patch by calling patch() with a target which is the
            get() method of the requests object in the utils module
        """
        # start the patcher called get_patcher
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()
        # use side_effect to make sure the mock of requests.get(url).json() -
        # returns the correct fixtures for the various values of url
        cls.mock_get.return_value.json.side_effect = [
            cls.org_payload,
            cls.repos_payload,
            cls.org_payload,
            cls.repos_payload
        ]

    @classmethod
    def tearDownClass(cls):
        """ A class method that does automatically clean up
        after all test methods have been executed"""
        # stop the get_patcher
        cls.get_patcher.stop()

    def test_public_repos(self):
        """ An integration test for the GithubOrgClient.public_repos method """
        github_org_client = GithubOrgClient("google")
        self.assertEqual(github_org_client.public_repos(), self.expected_repos)
        self.mock_get.assert_called()

    def test_public_repos_with_license(self):
        """Test the public_repos with the argument license='apache-2.0'"""
        github_org_client = GithubOrgClient('google')
        actual_repos = github_org_client.public_repos(license='apache-2.0')
        self.assertEqual(actual_repos, self.apache2_repos)
        self.mock_get.assert_called()


if __name__ == "__main__":
    unittest.main()
