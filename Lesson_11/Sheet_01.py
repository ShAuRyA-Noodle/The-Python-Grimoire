class Employee:
    """
    Represents an employee with first and last name handling using
    property decorators, along with a class-level attribute demonstration.

    Attributes:
        a (int): A class-level attribute shared among all Employee instances.
        fname (str): First name of the employee.
        lname (str): Last name of the employee.
    """

    # Class attribute shared across all instances
    a: int = 1

    def __init__(self, fname: str = "", lname: str = "") -> None:
        """
        Initialize an Employee instance.

        Args:
            fname (str, optional): First name of the employee.
            lname (str, optional): Last name of the employee.
        """
        self.fname = fname
        self.lname = lname

    @classmethod
    def show(cls) -> None:
        """
        Display the value of the class-level attribute `a`.

        This method accesses the attribute using the class reference (cls),
        ensuring that it always reflects the current class-level value.
        """
        print(f"The class attribute 'a' is currently set to: {cls.a}")

    @property
    def name(self) -> str:
        """
        Retrieve the employee's full name.

        Returns:
            str: A formatted string combining first and last name.
        """
        return f"{self.fname} {self.lname}".strip()

    @name.setter
    def name(self, value: str) -> None:
        """
        Set the employee's first and last name using a full-name string.

        Args:
            value (str): Full name consisting of first and last name
                         separated by a space.

        Raises:
            ValueError: If the provided name does not contain at least
                        two components.
        """
        parts = value.strip().split(" ")

        if len(parts) < 2:
            raise ValueError("Full name must include at least first and last name.")

        self.fname = parts[0]
        self.lname = parts[1]


# Example usage
if __name__ == "__main__":
    employee = Employee()

    # Setting full name using property setter
    employee.name = "Harry Khan"

    print(employee.fname, employee.lname)

    # Demonstrating class method
    employee.show()
