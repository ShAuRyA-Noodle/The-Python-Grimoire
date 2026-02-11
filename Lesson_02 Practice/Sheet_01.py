"""
addition_example.py
-------------------

This script demonstrates a simple arithmetic operation in Python by adding
two integer values and printing the result. It is a basic example used to
illustrate variables, expressions, and console output.
"""


# ---------------------------------------------------------------------
# CORE FUNCTION
# ---------------------------------------------------------------------

def add_numbers(x: int, y: int) -> int:
    """
    Return the sum of two integers.

    Args:
        x: First integer
        y: Second integer

    Returns:
        Sum of x and y
    """
    return x + y


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    a = 1
    b = 5

    result = add_numbers(a, b)
    print(f"The sum of {a} and {b} is: {result}")


if __name__ == "__main__":
    main()
