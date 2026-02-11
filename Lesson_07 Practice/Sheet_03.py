"""
centered_pyramid_pattern.py
---------------------------

This script prints a centered pyramid star (*) pattern based on the
number of rows entered by the user. It demonstrates spacing alignment,
string multiplication, and loop-based pattern generation.
"""


# ---------------------------------------------------------------------
# CORE FUNCTION
# ---------------------------------------------------------------------

def print_centered_pyramid(rows: int) -> None:
    """
    Print a centered pyramid pattern of stars.

    Args:
        rows: Number of rows in the pyramid
    """
    for i in range(1, rows + 1):
        spaces = " " * (rows - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    try:
        n = int(input("Enter the number: "))
        print_centered_pyramid(n)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")


if __name__ == "__main__":
    main()
