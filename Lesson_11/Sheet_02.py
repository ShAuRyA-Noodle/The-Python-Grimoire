class Employee:
    """
    Base class representing a generic employee.

    Attributes:
        a (int): A class-level attribute defined in the base class.
                 This attribute is inherited by all subclasses unless overridden.
    """
    a: int = 1


class Programmer(Employee):
    """
    Intermediate subclass representing a programmer.

    Inherits:
        Employee: Gains access to attribute 'a'.

    Attributes:
        b (int): A class-level attribute specific to the Programmer class.
    """
    b: int = 2


class Manager(Programmer):
    """
    Subclass representing a manager role.

    Inherits:
        Programmer: Gains access to attributes 'a' and 'b'.
        Employee: Gains access to attribute 'a' through the inheritance chain.

    Attributes:
        c (int): A class-level attribute specific to the Manager class.
    """
    c: int = 3


if __name__ == "__main__":
    # Instance of the base class
    employee = Employee()
    print(employee.a)  
    # Prints attribute 'a' because it is defined in the Employee class.
    # Accessing employee.b would raise an AttributeError because Employee
    # does not define attribute 'b'.

    # Instance of the Programmer subclass
    programmer = Programmer()
    print(programmer.a, programmer.b)
    # The Programmer instance can access:
    # - 'a' inherited from Employee
    # - 'b' defined in Programmer

    # Instance of the Manager subclass
    manager = Manager()
    print(manager.a, manager.b, manager.c)
    # The Manager instance can access:
    # - 'a' inherited from Employee
    # - 'b' inherited from Programmer
    # - 'c' defined in Manager
