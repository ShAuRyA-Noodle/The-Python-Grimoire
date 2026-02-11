"""
hollow_square_pattern.py
------------------------

This script prints a hollow square star (*) pattern of size `n`.
It demonstrates conditional logic inside loops and spacing control
for pattern generation.
"""


# ---------------------------------------------------------------------
# CORE FUNCTION
# ---------------------------------------------------------------------

def print_hollow_square(n: int) -> None:
    """
    Print a hollow square pattern of size n.

    Args:
        n: Size of the square
    """
    for i in range(1, n + 1):
        if i == 1 or i == n:
            print("*" * n)
        else:
            print("*" + " " * (n - 2) + "*")


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    try:
        n = int(input("Enter the number: "))
        print_hollow_square(n)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")


if __name__ == "__main__":
    main()
