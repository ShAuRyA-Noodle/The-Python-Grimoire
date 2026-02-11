from math import sqrt


class Calculator:
    """
    A simple mathematical calculator that performs operations
    on a single numeric value.

    Attributes:
        number (float): The numeric value on which calculations are performed.
    """

    def __init__(self, number: float) -> None:
        """
        Initialize the Calculator with a numeric value.

        Args:
            number (float): The value to be used for all mathematical operations.
        """
        self.number = number

    def square(self) -> float:
        """
        Compute the square of the stored number.

        Returns:
            float: The square of the number.
        """
        return self.number ** 2

    def cube(self) -> float:
        """
        Compute the cube of the stored number.

        Returns:
            float: The cube of the number.
        """
        return self.number ** 3

    def square_root(self) -> float:
        """
        Compute the square root of the stored number.

        Returns:
            float: The square root of the number.
        """
        return sqrt(self.number)


# Example usage (executed only when run as a script)
if __name__ == "__main__":
    calculator = Calculator(4)

    print(f"Square: {calculator.square()}")
    print(f"Cube: {calculator.cube()}")
    print(f"Square Root: {calculator.square_root()}")
