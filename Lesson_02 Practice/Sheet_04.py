"""
modulus_operation_demo.py
-------------------------

This script demonstrates the use of the modulus (%) operator in Python,
which returns the remainder after division of one number by another.

Use cases:
- Determining even/odd numbers
- Cyclic operations
- Hashing and indexing calculations
"""


# ---------------------------------------------------------------------
# CORE FUNCTION
# ---------------------------------------------------------------------

def calculate_remainder(dividend: int, divisor: int) -> int:
    """
    Calculate the remainder when one integer is divided by another.

    Args:
        dividend: The number being divided
        divisor: The number dividing the dividend

    Returns:
        The remainder of the division
    """
    return dividend % divisor


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    a = 37
    b = 5

    remainder = calculate_remainder(a, b)
    print(f"Remainder when {a} is divided by {b} is: {remainder}")


if __name__ == "__main__":
    main()
