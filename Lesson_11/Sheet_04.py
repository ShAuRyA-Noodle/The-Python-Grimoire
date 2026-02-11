class Employee:
    """
    Represents a general employee within an organization.

    Attributes:
        company (str): Name of the organization where the employee works.
        name (str): Default employee name (can be overridden per instance).
    """

    company: str = "ITC"
    name: str = "Default Name"

    def show(self) -> None:
        """
        Display the employee's name and associated company.
        """
        print(
            f"The name of the employee is '{self.name}' "
            f"and the company is '{self.company}'."
        )


class Coder:
    """
    Represents programming-related capabilities of an individual.

    Attributes:
        language (str): Primary programming language known by the coder.
    """

    language: str = "Python"

    def print_languages(self) -> None:
        """
        Display the coder's primary programming language.
        """
        print(
            f"The primary programming language assigned is: '{self.language}'."
        )


class Programmer(Employee, Coder):
    """
    Represents a programmer role combining employee details and
    coding capabilities through multiple inheritance.

    Inherits:
        Employee: Provides employee-related attributes and methods.
        Coder: Provides programming-language-related attributes and methods.

    Attributes:
        company (str): Overrides the base Employee company attribute to reflect
                       the specific organizational division.
    """

    company: str = "ITC Infotech"

    def show_language_profile(self) -> None:
        """
        Display the programmer's company and programming language expertise.
        """
        print(
            f"The programmer works at '{self.company}' "
            f"and specializes in '{self.language}'."
        )


# Example usage
if __name__ == "__main__":
    employee = Employee()
    programmer = Programmer()

    programmer.show()
    programmer.print_languages()
    programmer.show_language_profile()
