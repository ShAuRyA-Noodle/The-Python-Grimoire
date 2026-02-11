"""
recursive_pattern.py
--------------------

This script prints a decreasing star (*) pattern using recursion.

Example for n = 3:
***
**
*
"""


# ---------------------------------------------------------------------
# CORE FUNCTION
# ---------------------------------------------------------------------

def print_pattern(n: int) -> None:
    """
    Recursively print a decreasing star pattern.

    Args:
        n: Number of stars in the first row
    """
    if n == 0:
        return

    print("*" * n)
    print_pattern(n - 1)


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    print_pattern(3)


if __name__ == "__main__":
    main()
