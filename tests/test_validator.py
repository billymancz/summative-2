"""
Unit tests for the validation functions in validator.py.
"""

import unittest
import sys
import os

# Add the parent directory to the Python path to allow module imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from validator import is_valid_employee_id, is_present

class TestValidator(unittest.TestCase):
    """
    Contains tests for the input validation functions.
    """

    def test_is_valid_employee_id(self):
        """
        Tests the is_valid_employee_id function with various inputs.
        """
        self.assertTrue(is_valid_employee_id("12345"))
        self.assertTrue(is_valid_employee_id("0"))
        self.assertFalse(is_valid_employee_id("abc"))
        self.assertFalse(is_valid_employee_id("12a34"))
        self.assertFalse(is_valid_employee_id("12.34"))
        self.assertFalse(is_valid_employee_id("-123"))
        self.assertFalse(is_valid_employee_id(""))
        self.assertFalse(is_valid_employee_id("   "))
        self.assertFalse(is_valid_employee_id(" 123 "))

    def test_is_present(self):
        """
        Tests the is_present function with various inputs.
        """
        self.assertTrue(is_present("hello"))
        self.assertTrue(is_present("  hello  "))
        self.assertTrue(is_present("0"))
        self.assertFalse(is_present(""))
        self.assertFalse(is_present("   "))
        self.assertFalse(is_present(None))

if __name__ == '__main__':
    unittest.main()
