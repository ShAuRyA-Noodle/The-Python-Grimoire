"""
employee_class_with_init.py
---------------------------

This script demonstrates:

- Class attributes (shared across all instances)
- Instance attributes initialized via the constructor (__init__)
- Instance methods
- Static methods
"""


# ---------------------------------------------------------------------
# CLASS DEFINITION
# ---------------------------------------------------------------------

class Employee:
    # Class attributes (shared)
    language = "Python"
    salary = 1_200_000

    def __init__(self, name: str, salary: int = None, language: str = None):
        """
        Constructor (dunder method) called when an instance is created.

        Args:
            name: Name of the employee (required)
            salary: Salary of the employee (optional, defaults to class attribute)
            language: Programming language (optional, defaults to class attribute)
        """
        self.name = name
        self.salary = salary if salary is not None else Employee.salary
        self.language = language if language is not None else Employee.language
        print(f"Creating an Employee object for {self.name}")

    def get_info(self) -> None:
        """Print information about the employee."""
        print(f"Name: {self.name}, Language: {self.language}, Salary: {self.salary}")

    @staticmethod
    def greet() -> None:
        """Static method to greet."""
        print("Good morning")


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    # Creating an instance with custom values
    harry = Employee("Harry", 1_300_000, "JavaScript")
    harry.get_info()  # Access instance info
    Employee.greet()  # Static method can be called via class

    # Creating an instance with default salary and language
    rohan = Employee("Rohan")
    rohan.get_info()


if __name__ == "__main__":
    main()
