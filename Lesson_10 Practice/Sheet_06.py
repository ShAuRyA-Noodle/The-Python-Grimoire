class Programmer:
    """
    Represents a programmer working at a specific company.

    Attributes:
        company (str): Class-level attribute representing the organization
                       where all Programmer instances are employed.
        name (str): Name of the programmer.
        salary (float): Annual salary of the programmer.
        pin (int): Postal/identification PIN associated with the programmer.
    """

    # Class attribute shared across all instances
    company: str = "Microsoft"

    def __init__(self, name: str, salary: float, pin: int) -> None:
        """
        Initialize a Programmer instance with personal and compensation details.

        Args:
            name (str): The full name of the programmer.
            salary (float): The programmer's salary.
            pin (int): The PIN or location code associated with the programmer.
        """
        self.name = name
        self.salary = salary
        self.pin = pin

    def get_profile(self) -> str:
        """
        Return a formatted string containing the programmer's profile details.

        Returns:
            str: A formatted representation of the programmer's information.
        """
        return (
            f"Name: {self.name}, "
            f"Salary: {self.salary}, "
            f"PIN: {self.pin}, "
            f"Company: {self.company}"
        )


# Example usage (executed only when run directly)
if __name__ == "__main__":
    programmer_1 = Programmer("Harry", 1200000, 245001)
    programmer_2 = Programmer("Rohan", 1200000, 245001)

    print(programmer_1.get_profile())
    print(programmer_2.get_profile())
