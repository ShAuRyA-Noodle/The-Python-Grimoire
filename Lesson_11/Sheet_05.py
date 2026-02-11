class Employee:
    """
    Base class representing a generic employee.

    Attributes:
        a (int): Class-level attribute defined in the Employee class.
    """

    a: int = 1

    def __init__(self) -> None:
        """
        Initialize the Employee class.
        """
        print("Constructor of Employee")


class Programmer(Employee):
    """
    Intermediate subclass representing a programmer.

    Inherits:
        Employee: Gains access to attribute 'a' and Employee initialization.

    Attributes:
        b (int): Class-level attribute specific to the Programmer class.
    """

    b: int = 2

    def __init__(self) -> None:
        """
        Initialize the Programmer class while ensuring the Employee
        constructor is executed using super().
        """
        super().__init__()
        print("Constructor of Programmer")


class Manager(Programmer):
    """
    Final subclass representing a manager role.

    Inherits:
        Programmer: Gains access to attributes 'a' and 'b'.
        Employee: Gains access to attribute 'a' through the inheritance chain.

    Attributes:
        c (int): Class-level attribute specific to the Manager class.
    """

    c: int = 3

    def __init__(self) -> None:
        """
        Initialize the Manager class and ensure all parent constructors
        are executed in the proper Method Resolution Order (MRO).
        """
        super().__init__()
        print("Constructor of Manager")


# Example usage
if __name__ == "__main__":
    manager = Manager()
    print(manager.a, manager.b, manager.c)
