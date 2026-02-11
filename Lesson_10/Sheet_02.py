"""
employee_class_advanced.py
--------------------------

This script demonstrates Python class features including:

- Class attributes (shared across all instances)
- Instance methods (operate on object-specific data)
- Static methods (utility methods that do not depend on instance)
"""


# ---------------------------------------------------------------------
# CLASS DEFINITION
# ---------------------------------------------------------------------

class Employee:
    # Class attributes (shared by all instances unless overridden)
    language = "Python"
    salary = 1_200_000

    # -----------------------------------------------------------------
    # INSTANCE METHOD
    # -----------------------------------------------------------------
    def get_info(self) -> None:
        """
        Print information about the employee using instance and class attributes.
        """
        print(f"The language is {self.language}. The salary is {self.salary}")

    # -----------------------------------------------------------------
    # STATIC METHOD
    # -----------------------------------------------------------------
    @staticmethod
    def greet() -> None:
        """
        A static method that prints a greeting. Does not require 'self'.
        """
        print("Good morning")


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    # Create an instance of Employee
    harry = Employee()

    # Call static method (can be called on instance or class)
    harry.greet()           # Using instance
    Employee.greet()        # Using class (preferred)

    # Call instance method
    harry.get_info()

    # Alternative way to call instance method via class (explicit instance)
    Employee.get_info(harry)


if __name__ == "__main__":
    main()
