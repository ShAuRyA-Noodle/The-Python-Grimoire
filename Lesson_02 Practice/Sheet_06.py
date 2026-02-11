"""
square_calculator.py
--------------------

This script accepts an integer input from the user and calculates its
square using two equivalent approaches:
1. Exponentiation operator (**)
2. Multiplication (a * a)

It also highlights that the '^' operator in Python represents a
bitwise XOR operation, not exponentiation.
"""


# ---------------------------------------------------------------------
# CORE FUNCTION
# ---------------------------------------------------------------------

def calculate_square(number: int) -> int:
    """
    Calculate the square of a number.

    Args:
        number: Integer value whose square is to be calculated

    Returns:
        The square of the number
    """
    return number ** 2


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    try:
        a = int(input("Enter your number: "))

        square_exp = calculate_square(a)
        square_mul = a * a

        print(f"The square of the number using exponentiation is: {square_exp}")
        print(f"The square of the number using multiplication is: {square_mul}")

    except ValueError:
        print("Invalid input. Please enter a valid integer.")


if __name__ == "__main__":
    main()
