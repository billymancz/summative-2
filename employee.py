"""
Defines the Employee class, which represents a single employee record.
"""

class Employee:
    """
    Represents an employee with their personal and employment details.

    Attributes:
        employee_id (str): The unique identifier for the employee.
        first_name (str): The first name of the employee.
        last_name (str): The last name of the employee.
        department (str): The department where the employee works.
        job_title (str): The job title of the employee.
    """
    def __init__(self, employee_id: str, first_name: str, last_name: str, department: str, job_title: str):
        """
        Initializes an Employee object.

        Args:
            employee_id (str): The employee's unique ID.
            first_name (str): The employee's first name.
            last_name (str): The employee's last name.
            department (str): The employee's department.
            job_title (str): The employee's job title.
        """
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.department = department
        self.job_title = job_title

    def to_list(self) -> list[str]:
        """
        Returns the employee's details as a list of strings.

        Returns:
            list[str]: A list containing the employee's ID, first name,
                       last name, department, and job title.
        """
        return [
            self.employee_id,
            self.first_name,
            self.last_name,
            self.department,
            self.job_title
        ]

    def __str__(self) -> str:
        """
        Returns a string representation of the Employee object.

        Returns:
            str: A string summarizing the employee's details.
        """
        return (f"Employee(ID: {self.employee_id}, Name: {self.first_name} "
                f"{self.last_name}, Department: {self.department})")
