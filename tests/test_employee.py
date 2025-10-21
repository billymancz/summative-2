"""
Unit tests for the Employee class in employee.py.
"""

import unittest
import sys
import os

# Add the parent directory to the Python path to allow module imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from employee import Employee

class TestEmployee(unittest.TestCase):
    """
    Contains tests for the Employee data model class.
    """

    def setUp(self):
        """
        Set up a sample Employee object that can be used in all tests.
        This method is called before each test function is executed.
        """
        self.employee = Employee(
            employee_id="101",
            first_name="Jane",
            last_name="Doe",
            department="Engineering",
            job_title="Software Developer"
        )

    def test_employee_initialization(self):
        """
        Tests if the Employee object is initialized with the correct attributes.
        """
        self.assertEqual(self.employee.employee_id, "101")
        self.assertEqual(self.employee.first_name, "Jane")
        self.assertEqual(self.employee.last_name, "Doe")
        self.assertEqual(self.employee.department, "Engineering")
        self.assertEqual(self.employee.job_title, "Software Developer")

    def test_to_list(self):
        """
        Tests the to_list method to ensure it returns data in the correct order and format.
        """
        expected_list = ["101", "Jane", "Doe", "Engineering", "Software Developer"]
        self.assertEqual(self.employee.to_list(), expected_list)

    def test_str_representation(self):
        """
        Tests the __str__ method for a correct and readable string representation.
        """
        expected_str = "Employee(ID: 101, Name: Jane Doe, Department: Engineering)"
        self.assertEqual(str(self.employee), expected_str)

if __name__ == '__main__':
    unittest.main()
