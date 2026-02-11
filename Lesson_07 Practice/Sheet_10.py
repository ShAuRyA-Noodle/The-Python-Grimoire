"""
factorial_calculator.py
-----------------------

This script calculates the factorial of a given number using an
iterative approach. It demonstrates loop-based multiplication,
input validation, and formatted output.

Factorial definition:
n! = 1 × 2 × 3 × ... × n
"""


# ---------------------------------------------------------------------
# CORE FUNCTION
# ---------------------------------------------------------------------

def calculate_factorial(n: int) -> int:
    """
    Calculate the factorial of a number.

    Args:
        n: Non-negative integer

    Returns:
        Factorial of n
    """
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    try:
        n = int(input("Enter the number: "))

        if n < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            factorial = calculate_factorial(n)
            print(f"The factorial of {n} is {factorial}")

    except ValueError:
        print("Invalid input. Please enter a valid integer.")


if __name__ == "__main__":
    main()
