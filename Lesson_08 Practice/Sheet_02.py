"""
greatest_number_function.py
---------------------------

This script defines a function to determine the greatest of three
numbers using Python's built-in `max()` function.
"""


# ---------------------------------------------------------------------
# CORE FUNCTION
# ---------------------------------------------------------------------

def greatest(a: int, b: int, c: int) -> int:
    """
    Return the greatest of three numbers.

    Args:
        a: First number
        b: Second number
        c: Third number

    Returns:
        Largest number among the three
    """
    return max(a, b, c)


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    a = 1
    b = 23
    c = 3

    print(greatest(a, b, c))


if __name__ == "__main__":
    main()
