"""
sum_natural_numbers.py
----------------------

This script calculates the sum of the first `n` natural numbers using a
while loop. It demonstrates loop-controlled accumulation and input
validation.
"""


# ---------------------------------------------------------------------
# CORE FUNCTION
# ---------------------------------------------------------------------

def calculate_sum(n: int) -> int:
    """
    Calculate the sum of the first n natural numbers.

    Args:
        n: Upper limit of natural numbers

    Returns:
        Sum of numbers from 1 to n
    """
    i = 1
    total = 0

    while i <= n:
        total += i
        i += 1

    return total


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    try:
        n = int(input("Enter the number: "))
        result = calculate_sum(n)
        print(f"Sum of first {n} natural numbers is: {result}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")


if __name__ == "__main__":
    main()
