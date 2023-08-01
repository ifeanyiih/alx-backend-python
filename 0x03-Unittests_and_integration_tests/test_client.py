#!/usr/bin/env python3
"""
Script contains a test case TestGithubOrgClient class
that implements a method to test that client.GithubOrgClient
returns the correct value
"""
import unittest
from unittest.mock import patch, Mock, PropertyMock
from client import GithubOrgClient
from parameterized import parameterized
from fixtures import TEST_PAYLOAD

json = TEST_PAYLOAD[0][1]


class TestGithubOrgClient(unittest.TestCase):
    """A unittest test case"""
    @parameterized.expand([
        ('google', json),
        ('abc', json)
    ])
    @patch('client.get_json')
    def test_org(self, expr, res, mock):
        """Mocks an object and checks that
        it is called as it should"""
        mock.return_value = json
        obj = GithubOrgClient(expr)
        self.assertEqual(obj.org, res)
        self.assertEqual(obj.org, res)
        mock.assert_called_once_with(obj.ORG_URL.format(org=expr))

    def test_public_repos_url(self):
        """test Mocks a property and
        makes sure that the payload is the
        expected one"""
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock:
            mock.return_value = TEST_PAYLOAD[0][0]
            obj = GithubOrgClient('google')
            self.assertEqual(obj._public_repos_url, mock()['repos_url'])

    @patch('client.get_json')
    def test_public_repos(self, mock):
        """mock objects and check their calls"""
        mock.return_value = TEST_PAYLOAD[0][1]
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as pmock:
            pmock.return_value = TEST_PAYLOAD[0][0]['repos_url']
            obj = GithubOrgClient('google')
            obj.public_repos()
            pmock.assert_called_once()
            mock.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license"),
        ({"license": {"key": "other_license"}}, "my_license")
    ])
    def test_has_license(self, repo, key):
        """Parameterizes a test with inputs"""
        GithubOrgClient.has_license(repo, key)
