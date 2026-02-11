"""
sum_two_numbers.py
------------------

This script accepts two integer inputs from the user and prints their
values along with their sum. It demonstrates basic console input,
type conversion, and arithmetic operations in Python.
"""


# ---------------------------------------------------------------------
# CORE FUNCTION
# ---------------------------------------------------------------------

def calculate_sum(a: int, b: int) -> int:
    """
    Calculate the sum of two integers.

    Args:
        a: First integer value
        b: Second integer value

    Returns:
        The sum of the two integers
    """
    return a + b


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    """
    Collect user input, compute the sum, and display results.
    """
    try:
        a = int(input("Enter number 1: "))
        b = int(input("Enter number 2: "))

        total = calculate_sum(a, b)

        print(f"Number a is: {a}")
        print(f"Number b is: {b}")
        print(f"Sum is: {total}")

    except ValueError:
        print("Invalid input. Please enter valid integer numbers.")


if __name__ == "__main__":
    main()
