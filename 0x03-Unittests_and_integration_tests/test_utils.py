#!/usr/bin/env python3
"""Script contains a test case TestAccessNestedMap
class that implements a method to test that
utils.access_nested_map returns what it is supposed to
"""
import unittest
from unittest.mock import patch, Mock
from utils import access_nested_map, requests, get_json
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """A unittest test case"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """tests that the method returns what it is
        supposed to"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """tests that the right errors are raised"""
        self.assertRaises(expected, access_nested_map, nested_map, path)


class TestGetJson(unittest.TestCase):
    """A unittest test case"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url, payload):
        """tests that utils.get_json returns the
        expected result"""
        with patch('requests.get') as requestGetMock:
            mock = Mock()
            mock.json.return_value = payload
            requestGetMock.return_value = mock
            self.assertEqual(get_json(url), payload)
            requestGetMock.assert_called_once_with(url)
