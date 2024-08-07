# Author: Jake Trissel
# Github Username: trisselj
# Date: 08/07/2024
# Description: Creates a dictionary of employees with there names IDs salaries and email addresses with get commands

# Initializes data set with employee name, ID, salary, and email
class Employee:
    def __init__(self, name, ID_number, salary, email_address): 
        self.__name = name
        self.__ID_number = ID_number
        self.__salary = salary
        self.__email_address = email_address

    # Returns name, ID, salary, and email
    def get_name(self):
        return self.__name
    
    def get_ID_number(self):
        return self.__ID_number
    
    def get_salary(self):
        return self.__salary
    
    def get_salary(self):
        return self.__salary
    
# Creates empty dictionary for storing Employees
def make_employee_dict(names, ids, salaries, emails):
    employee_dict = {}

    # Loops through each index to creat the Employee objects
    for name, ID, salary, email in zip(names, ids, salaries, emails):
        employee = Employee(name, ID, salary, email) # Creates the employee object
        employee_dict[ID] = employee # Adds the employee to the dictionary using ID as key
    return employee_dict
