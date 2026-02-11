"""
employee_instance_vs_class.py
-----------------------------

This script demonstrates the difference between **class attributes**
(shared across all instances) and **instance attributes** (specific to
each object).
"""


# ---------------------------------------------------------------------
# CLASS DEFINITION
# ---------------------------------------------------------------------

class Employee:
    # Class attributes (shared by all instances)
    language = "Python"
    salary = 1_200_000


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    # Create first employee instance
    harry = Employee()
    harry.name = "Harry"  # Instance attribute

    # Access instance and class attributes
    print(f"{harry.name}, Language: {harry.language}, Salary: {harry.salary}")

    # Create second employee instance
    rohan = Employee()
    rohan.name = "Rohan Roro Robinson"  # Instance attribute

    # Access instance and class attributes
    print(f"{rohan.name}, Salary: {rohan.salary}, Language: {rohan.language}")

    # Note: 'name' is specific to the instance
    #       'language' and 'salary' are shared class attributes


if __name__ == "__main__":
    main()
