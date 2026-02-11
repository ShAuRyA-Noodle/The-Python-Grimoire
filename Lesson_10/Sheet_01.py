"""
employee_class_demo.py
----------------------

This script demonstrates the difference between **class attributes** and
**instance attributes** in Python classes.
"""


# ---------------------------------------------------------------------
# CLASS DEFINITION
# ---------------------------------------------------------------------

class Employee:
    # Class attributes (shared across all instances unless overridden)
    language = "Python"
    salary = 1_200_000


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    # Create an instance of Employee
    harry = Employee()

    # Override the class attribute with an instance attribute
    harry.language = "JavaScript"  # Instance attribute

    # Access attributes
    print(f"Language: {harry.language}")  # Instance attribute
    print(f"Salary: {harry.salary}")      # Class attribute


if __name__ == "__main__":
    main()
