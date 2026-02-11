"""
recursive_factorial.py
----------------------

This script calculates the factorial of a number using recursion.

Mathematical definition:
factorial(n) = n × factorial(n - 1)
Base cases:
factorial(0) = 1
factorial(1) = 1
"""


# ---------------------------------------------------------------------
# CORE FUNCTION
# ---------------------------------------------------------------------

def factorial(n: int) -> int:
    """
    Calculate factorial recursively.

    Args:
        n: Non-negative integer

    Returns:
        Factorial of n
    """
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    try:
        number = int(input("Enter a number: "))

        if number < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            print(f"The factorial of this number is: {factorial(number)}")

    except ValueError:
        print("Invalid input. Please enter a valid integer.")


if __name__ == "__main__":
    main()
