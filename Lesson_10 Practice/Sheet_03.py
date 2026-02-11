"""
calculator_class.py
-------------------

This script defines a Calculator class that can compute:
- Square
- Cube
- Square root
It also includes a static method for greeting.
"""


# ---------------------------------------------------------------------
# CLASS DEFINITION
# ---------------------------------------------------------------------

class Calculator:
    """
    A simple calculator for basic operations on a single number.
    """

    def __init__(self, n: float):
        """
        Initialize the calculator with a number.

        Args:
            n: The number to operate on
        """
        self.n = n

    def square(self) -> None:
        """Print the square of the number."""
        print(f"The square of {self.n} is {self.n ** 2}")

    def cube(self) -> None:
        """Print the cube of the number."""
        print(f"The cube of {self.n} is {self.n ** 3}")

    def squareroot(self) -> None:
        """Print the square root of the number."""
        print(f"The square root of {self.n} is {self.n ** 0.5:.2f}")

    @staticmethod
    def hello() -> None:
        """Print a greeting message."""
        print("Hello there!")


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    calc = Calculator(4)
    
    # Call static method
    calc.hello()

    # Call instance methods
    calc.square()
    calc.cube()
    calc.squareroot()


if __name__ == "__main__":
    main()
