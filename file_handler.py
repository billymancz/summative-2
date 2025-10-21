"""
Handles reading from and writing to CSV files for employee data.
"""

import csv
import logging
from employee import Employee

class FileHandler:
    """
    A class to manage CSV file operations for employee records.
    """

    @staticmethod
    def read_employees(file_path: str) -> list[Employee]:
        """
        Reads employee data from a CSV file and returns a list of Employee objects.

        Args:
            file_path (str): The path to the CSV file.

        Returns:
            list[Employee]: A list of Employee objects.
        
        Raises:
            FileNotFoundError: If the specified file_path does not exist.
            Exception: For other potential I/O errors or data format issues.
        """
        employees = []
        try:
            with open(file_path, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try:
                        employee = Employee(
                            employee_id=row["employee_id"],
                            first_name=row["first_name"],
                            last_name=row["last_name"],
                            department=row["department"],
                            job_title=row["job_title"]
                        )
                        employees.append(employee)
                    except KeyError as e:
                        # Handle cases where a column is missing in a row
                        logging.warning(f"Skipping row due to missing column: {e}")
        except FileNotFoundError:
            # This allows the application to start even if the file doesn't exist yet.
            logging.info(f"The file {file_path} was not found. A new one will be created upon export.")
            return []
        except Exception as e:
            logging.error(f"An error occurred while reading the file: {e}")
            raise
        return employees

    @staticmethod
    def write_employees(file_path: str, employees: list[Employee]):
        """
        Writes a list of Employee objects to a CSV file.

        Args:
            file_path (str): The path to the CSV file to be written.
            employees (list[Employee]): The list of Employee objects to write.
        
        Raises:
            Exception: For potential I/O errors.
        """
        try:
            with open(file_path, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                # Write header
                writer.writerow(["employee_id", "first_name", "last_name", "department", "job_title"])
                # Write employee data
                for employee in employees:
                    writer.writerow(employee.to_list())
        except Exception as e:
            logging.error(f"An error occurred while writing to the file: {e}")
            raise
