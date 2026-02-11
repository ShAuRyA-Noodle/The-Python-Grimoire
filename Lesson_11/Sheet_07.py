class Employee:
    """
    Represents an employee class demonstrating the behavior of
    class attributes and class methods.

    Attributes:
        a (int): A class-level attribute shared across all instances
                 unless overridden at the instance level.
    """

    a: int = 1

    @classmethod
    def show(cls) -> None:
        """
        Display the current value of the class attribute `a`.

        The method uses the class reference (`cls`) rather than an
        instance reference, ensuring that the value shown always
        reflects the class-level attribute rather than any instance-
        level attribute that may shadow it.
        """
        print(f"The class attribute 'a' is currently set to: {cls.a}")


# Example usage
if __name__ == "__main__":
    employee = Employee()

    # Creating an instance attribute that shadows the class attribute
    employee.a = 45

    # Calling the class method still accesses the class-level attribute
    employee.show()
