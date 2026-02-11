"""
simple_addition.py
------------------

This script demonstrates a basic arithmetic operation in Python by adding
two integer values and printing the result. It serves as an introductory
example for variables and arithmetic expressions.
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
        The sum of x and y
    """
    return x + y


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    a = 1
    b = 2
    c = 7
    name = "harry"

    result = add_numbers(a, b)
    print(f"The sum of {a} and {b} is: {result}")


if __name__ == "__main__":
    main()
