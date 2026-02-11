class Employee:
    """
    Represents an employee compensation model that supports
    automatic calculation of salary after increment using
    property decorators.

    Attributes:
        salary (float): Base salary of the employee.
        increment (float): Increment percentage applied to the salary.
    """

    def __init__(self, salary: float = 234.0, increment: float = 20.0) -> None:
        """
        Initialize the Employee instance.

        Args:
            salary (float): Base salary of the employee.
            increment (float): Increment percentage.
        """
        self.salary = salary
        self.increment = increment

    @property
    def salary_after_increment(self) -> float:
        """
        Calculate the salary after applying the increment.

        Returns:
            float: Updated salary after increment.
        """
        return self.salary * (1 + self.increment / 100)

    @salary_after_increment.setter
    def salary_after_increment(self, updated_salary: float) -> None:
        """
        Update the increment percentage based on a desired final salary.

        Args:
            updated_salary (float): Desired salary after increment.

        Raises:
            ValueError: If base salary is zero or negative.
        """
        if self.salary <= 0:
            raise ValueError("Base salary must be greater than zero.")

        self.increment = ((updated_salary / self.salary) - 1) * 100


# Example usage
if __name__ == "__main__":
    employee = Employee()

    # Set salary after increment and automatically compute increment percentage
    employee.salary_after_increment = 280.8

    print(f"Increment percentage: {employee.increment:.2f}%")
