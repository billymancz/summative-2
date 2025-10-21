"""
Main application file for the Employee Management System.

This file contains the GUI for the application, built using Tkinter.
It orchestrates the interactions between the user interface and the backend logic
(data handling, validation).
"""

import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

from employee import Employee
from file_handler import FileHandler
from validator import is_valid_employee_id, is_present

# Define the path for the data file relative to the script's location
# Get the directory where the script is located.
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# Define the path for the data file relative to the script's directory.
DATA_FILE = os.path.join(SCRIPT_DIR, "employees.csv")

class EmployeeApp(tk.Tk):
    """
    The main application class for the Employee Management System GUI.

    This class encapsulates the entire application, including the main window,
    widgets, and event handling logic.
    """

    def __init__(self):
        """
        Initialises the main application window and its components.
        """
        super().__init__()

        self.title("Employee Management System")
        self.geometry("900x600")

        self.employees: list[Employee] = []

        # --- Main Layout --- #
        main_frame = ttk.Frame(self, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # --- Employee Display Treeview --- #
        tree_frame = ttk.Frame(main_frame)
        tree_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        columns = ("ID", "First Name", "Last Name", "Department", "Job Title")
        self.tree = ttk.Treeview(tree_frame, columns=columns, show="headings")

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150)

        # Add a scrollbar
        scrollbar = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # --- Input Form for New Employees --- #
        form_frame = ttk.LabelFrame(main_frame, text="Add New Employee", padding="10")
        form_frame.pack(fill=tk.X, pady=10)

        self.entries = {}
        form_fields = ["Employee ID", "First Name", "Last Name", "Department", "Job Title"]
        for i, field in enumerate(form_fields):
            label = ttk.Label(form_frame, text=f"{field}:")
            label.grid(row=i, column=0, padx=5, pady=5, sticky=tk.W)
            entry = ttk.Entry(form_frame, width=40)
            entry.grid(row=i, column=1, padx=5, pady=5, sticky=tk.EW)
            self.entries[field] = entry
        
        form_frame.columnconfigure(1, weight=1)

        # --- Action Buttons --- #
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.X, pady=10)

        add_button = ttk.Button(button_frame, text="Add Employee", command=self.add_employee)
        add_button.pack(side=tk.LEFT, padx=5)

        export_button = ttk.Button(button_frame, text="Export to CSV", command=self.export_to_csv)
        export_button.pack(side=tk.LEFT, padx=5)

        # --- Status Bar --- #
        self.status_var = tk.StringVar()
        status_bar = ttk.Label(self, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W, padding="5")
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)

        # --- Initial Data Load --- #
        self.load_employees()

    def load_employees(self):
        """
        Loads employees from the CSV file and populates the treeview.
        Handles potential errors like the file not being found.
        """
        try:
            self.employees = FileHandler.read_employees(DATA_FILE)
            self.refresh_treeview()
            self.update_status(f"Loaded {len(self.employees)} employees from {DATA_FILE}")
        except Exception as e:
            messagebox.showerror("Error Loading Data", f"Failed to load employee data: {e}")
            self.update_status("Error: Could not load data.")

    def refresh_treeview(self):
        """
        Clears and repopulates the treeview with current employee data.
        """
        # Clear existing items
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Add new items
        for emp in self.employees:
            self.tree.insert("", tk.END, values=emp.to_list())

    def add_employee(self):
        """
        Validates input and adds a new employee to the list.
        Includes input validation and exception handling.
        """
        # --- Input Validation --- #
        emp_id = self.entries["Employee ID"].get()
        if not is_valid_employee_id(emp_id):
            messagebox.showerror("Invalid Input", "Employee ID must be a non-empty number.")
            return
        
        # Check if employee ID already exists
        if any(emp.employee_id == emp_id for emp in self.employees):
            messagebox.showerror("Invalid Input", f"Employee ID {emp_id} already exists.")
            return

        first_name = self.entries["First Name"].get()
        last_name = self.entries["Last Name"].get()
        department = self.entries["Department"].get()
        job_title = self.entries["Job Title"].get()

        if not all(map(is_present, [first_name, last_name, department, job_title])):
            messagebox.showerror("Invalid Input", "All fields must be filled out.")
            return

        # --- Add Employee --- #
        try:
            new_employee = Employee(emp_id, first_name, last_name, department, job_title)
            self.employees.append(new_employee)
            self.refresh_treeview()
            self.clear_form()
            self.update_status(f"Successfully added employee: {first_name} {last_name}")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {e}")
            self.update_status("Error: Could not add employee.")

    def export_to_csv(self):
        """
        Exports the current list of employees to a new CSV file.
        Asks the user for a file location to save to.
        """
        if not self.employees:
            messagebox.showwarning("No Data", "There is no employee data to export.")
            return

        try:
            file_path = filedialog.asksaveasfilename(
                defaultextension=".csv",
                filetypes=[("CSV files", "*.csv"), ("All files", "*.*")],
                title="Save Employee Data As"
            )
            if not file_path:
                self.update_status("Export cancelled.")
                return

            FileHandler.write_employees(file_path, self.employees)
            messagebox.showinfo("Export Successful", f"Data successfully exported to {file_path}")
            self.update_status(f"Exported {len(self.employees)} records to {file_path}")
        except Exception as e:
            messagebox.showerror("Export Error", f"Failed to export data: {e}")
            self.update_status("Error: Export failed.")

    def clear_form(self):
        """
        Clears all entry fields in the input form.
        """
        for entry in self.entries.values():
            entry.delete(0, tk.END)

    def update_status(self, message: str):
        """
        Updates the text in the status bar.

        Args:
            message (str): The message to display.
        """
        self.status_var.set(message)

if __name__ == "__main__":
    app = EmployeeApp()
    app.mainloop()
