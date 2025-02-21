# Author: Jake Trissel
# Github Username: trisselj
# Date: 08/07/2024
# Description: Creates a dictionary of employees with there names IDs salaries and email addresses with get commands

# Initializes data set with employee name, ID, salary, and email
class Employee:
    def __init__(self, name, ID_number, salary, email_address): 
        self._name = name
        self._ID_number = ID_number
        self._salary = salary
        self._email_address = email_address

    # Returns name, ID, salary, and email
    def get_name(self):
        return self._name
    
    def get_ID_number(self):
        return self._ID_number
    
    def get_salary(self):
        return self._salary
    
    def get_email_address(self):
        return self._email_address
    
# Creates empty dictionary for storing Employees
def make_employee_dict(_name, ID, Salary, Email):
    employee_dict = {}

    # Loops through each index to creat the Employee objects
    for name, ID, salary, email in zip(_name, ID, Salary, Email):
        employee = Employee(name, ID, salary, email) # Creates the employee object
        employee_dict[ID] = employee # Adds the employee to the dictionary using ID as key
    return employee_dict