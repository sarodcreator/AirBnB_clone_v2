#!/usr/bin/python3
"""Defines a class TestHBNBCommand"""
from console import HBNBCommand
import console
import pepe8
import unittest

class TestHBNBCommand(unittest.TestCase):
    """Tests for HBNBCommand
    """

    def test_class_docstr(self):
        """Tests for HBNBCommand class docstring.
        """
        self.assertTrue(len(HBNBCommand.__doc__) >= 1)

    def test_module_docstr(self):
        """Tests for the module docstring.
        """
        self.assertTrue(len(console.__doc__) >= 1)

    def test_testconsole_conforms_pep8(self):
        """Test that tests/test_console.py conforms to PEP8 guidelines.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["tests/test_console.py"])
        self.assertEqual(result.total_errors, 0, "Not to pep8 standard")

    def test_console_conforms_pep8(self):
        """Test if console.py conforms to PEP8 guidelines.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["console.py"])
        self.assertEqual(result.total_errors, 0, "Not to pep8 standard")
