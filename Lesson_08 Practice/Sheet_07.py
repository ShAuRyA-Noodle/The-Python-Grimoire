"""
recursive_sum_natural_numbers.py
--------------------------------

This script calculates the sum of the first n natural numbers using
recursion based on the relation:

sum(n) = sum(n - 1) + n
Base case:
sum(1) = 1
"""


# ---------------------------------------------------------------------
# CORE FUNCTION
# ---------------------------------------------------------------------

def sum_natural_numbers(n: int) -> int:
    """
    Recursively compute the sum of the first n natural numbers.

    Args:
        n: Positive integer

    Returns:
        Sum of numbers from 1 to n
    """
    if n <= 1:
        return n
    return sum_natural_numbers(n - 1) + n


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    print(sum_natural_numbers(4))


if __name__ == "__main__":
    main()
