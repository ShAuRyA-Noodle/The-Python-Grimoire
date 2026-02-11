class Employee:
    """
    Base class representing a general employee.

    Attributes:
        company (str): Default company name shared across Employee instances.
        name (str): Name of the employee.
        salary (float): Salary of the employee.
    """

    company: str = "ITC"

    def __init__(self, name: str, salary: float) -> None:
        """
        Initialize an Employee instance.

        Args:
            name (str): Employee's name.
            salary (float): Employee's salary.
        """
        self.name = name
        self.salary = salary

    def show(self) -> None:
        """
        Display the employee's name and salary details.
        """
        print(
            f"The name of the employee is '{self.name}' "
            f"and the salary is {self.salary}."
        )


class Programmer(Employee):
    """
    Subclass representing a programmer working in a specialized division.

    Inherits:
        Employee: Gains employee attributes and methods.

    Attributes:
        company (str): Overrides the base class company attribute.
        language (str): Primary programming language known by the programmer.
    """

    company: str = "ITC Infotech"

    def __init__(self, name: str, salary: float, language: str) -> None:
        """
        Initialize a Programmer instance.

        Args:
            name (str): Programmer's name.
            salary (float): Programmer's salary.
            language (str): Primary programming language.
        """
        super().__init__(name, salary)
        self.language = language

    def show_language(self) -> None:
        """
        Display the programmer's language expertise.
        """
        print(
            f"The programmer '{self.name}' is proficient in '{self.language}'."
        )


# Example usage
if __name__ == "__main__":
    employee = Employee("Rahul", 600000)
    programmer = Programmer("Aman", 900000, "Python")

    print(employee.company, programmer.company)
