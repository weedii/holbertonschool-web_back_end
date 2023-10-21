#!/usr/bin/env python3
"""Parameterize a unit test"""

from utils import access_nested_map, get_json
import unittest
from unittest.mock import patch
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """test for utils.access_nested_ma"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, result):
        """test_access_nested_map method test
        that the method returns what it is supposed to"""
        self.assertEqual(access_nested_map(nested_map, path), result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """test_access_nested_map_exception method
        that test that a KeyError is raised"""
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path)
        self.assertEqual(error.exception.args[0], path[-1])


class TestGetJson(unittest.TestCase):
    """test for utils.get_json"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url, payload):
        """test_get_json method that test that
        utils.get_json returns the expected result."""
        with patch("requests.get") as mock:
            mock.return_value = payload
            self.assertEqual(get_json(url), payload)
