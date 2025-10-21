"""
Provides pure functions for input validation.

These functions are designed to be testable and have no side effects, returning
the same output for the same input consistently.
"""

def is_valid_employee_id(employee_id: str) -> bool:
    """
    Validates if the employee ID is a non-empty string of digits.

    Args:
        employee_id (str): The employee ID to validate.

    Returns:
        bool: True if the employee_id is valid, False otherwise.
    """
    return employee_id.isdigit() and employee_id.strip() != ""

def is_present(text: str) -> bool:
    """
    Validates if the given text is not empty or just whitespace.

    Args:
        text (str): The string to validate.

    Returns:
        bool: True if the text is present, False otherwise.
    """
    return text is not None and text.strip() != ""
