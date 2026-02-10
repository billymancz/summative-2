"""
Unit tests for the FileHandler class in file_handler.py using mocking.
"""

import unittest
from unittest.mock import patch, mock_open, MagicMock
import sys
import os
import csv

# Add the parent directory to the Python path to allow module imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from file_handler import FileHandler
from employee import Employee

class TestFileHandler(unittest.TestCase):
    """
    Contains tests for the FileHandler class, using mocks to isolate
    the file system dependencies.
    """

    def setUp(self):
        """
        Set up common data to be used across tests.
        """
        self.employees_list = [
            Employee("101", "Jane", "Doe", "Engineering", "Developer"),
            Employee("102", "John", "Smith", "Marketing", "Manager")
        ]

    @patch("builtins.open", new_callable=mock_open, read_data='employee_id,first_name,last_name,department,job_title\n101,Jane,Doe,Engineering,Developer\n')
    def test_read_employees_success(self, mock_file):
        """
        Tests the successful reading and parsing of a CSV file.
        The 'open' function is mocked to return a fake file content.
        """
        file_path = "dummy/path/employees.csv"
        employees = FileHandler.read_employees(file_path)

        # Assert that 'open' was called with the correct path and mode
        mock_file.assert_called_once_with(file_path, mode='r', newline='', encoding='utf-8')

        # Assert the returned data is correct
        self.assertEqual(len(employees), 1)
        self.assertIsInstance(employees[0], Employee)
        self.assertEqual(employees[0].employee_id, "101")
        self.assertEqual(employees[0].first_name, "Jane")

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_read_employees_file_not_found(self, mock_file):
        """
        Tests that read_employees returns an empty list when FileNotFoundError is raised.
        """
        file_path = "non_existent_file.csv"
        employees = FileHandler.read_employees(file_path)

        # Assert that 'open' was called
        mock_file.assert_called_once_with(file_path, mode='r', newline='', encoding='utf-8')

        # Assert that the function returns an empty list as expected
        self.assertEqual(employees, [])

    @patch("builtins.open", new_callable=mock_open)
    def test_write_employees(self, mock_file):
        """
        Tests the successful writing of employee data to a CSV file.
        Mocks the file and the csv.writer to verify the data being written.
        """
        file_path = "dummy/path/output.csv"
        
        mock_writer = MagicMock()
        with patch('csv.writer', return_value=mock_writer):
            FileHandler.write_employees(file_path, self.employees_list)

            # Check that the file was opened for writing
            mock_file.assert_called_once_with(file_path, mode='w', newline='', encoding='utf-8')

            # Check that the header was written
            mock_writer.writerow.assert_any_call(["employee_id", "first_name", "last_name", "department", "job_title"])

            # Check that the employee data was written
            mock_writer.writerow.assert_any_call(["101", "Jane", "Doe", "Engineering", "Developer"])
            mock_writer.writerow.assert_any_call(["102", "John", "Smith", "Marketing", "Manager"])
            
            # Ensure writerow was called 3 times (1 for header, 2 for employees)
            self.assertEqual(mock_writer.writerow.call_count, 3)

if __name__ == '__main__':
    unittest.main()
