"""
right_triangle_pattern.py
-------------------------

This script prints a right-angled triangle star (*) pattern based on
user input. It demonstrates nested iteration concepts and string
multiplication for pattern generation.
"""


# ---------------------------------------------------------------------
# CORE FUNCTION
# ---------------------------------------------------------------------

def print_triangle_pattern(n: int) -> None:
    """
    Print a right-angled triangle star pattern.

    Args:
        n: Number of rows in the triangle
    """
    for i in range(1, n + 1):
        print("*" * i)


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    try:
        n = int(input("Enter the number: "))
        print_triangle_pattern(n)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")


if __name__ == "__main__":
    main()
