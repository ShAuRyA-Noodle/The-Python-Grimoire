"""
comparison_input_demo.py
------------------------

This script accepts two integer inputs from the user and determines whether
the first number is greater than the second. It demonstrates user input
handling, type conversion, comparison operators, and formatted output.
"""


# ---------------------------------------------------------------------
# CORE FUNCTION
# ---------------------------------------------------------------------

def is_greater(a: int, b: int) -> bool:
    """
    Determine whether the first number is greater than the second.

    Args:
        a: First integer
        b: Second integer

    Returns:
        True if a > b, otherwise False
    """
    return a > b


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    try:
        a = int(input("Enter number 1: "))
        b = int(input("Enter number 2: "))

        result = is_greater(a, b)
        print(f"a is greater than b: {result}")

    except ValueError:
        print("Invalid input. Please enter valid integer values.")


if __name__ == "__main__":
    main()
