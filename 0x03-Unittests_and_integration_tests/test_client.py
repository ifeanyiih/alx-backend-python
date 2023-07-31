#!/usr/bin/env python3
"""
Script contains a test case TestGithubOrgClient class
that implements a method to test that client.GithubOrgClient
returns the correct value
"""
import unittest
from unittest.mock import patch, Mock
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
        """"""
        mock.return_value = json
        obj = GithubOrgClient(expr)
        self.assertEqual(obj.org, res)
        self.assertEqual(obj.org, res)
        mock.assert_called_once_with(obj.ORG_URL.format(org=expr))
