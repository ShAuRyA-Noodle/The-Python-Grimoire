"""
multiplication_table_function.py
--------------------------------

This script defines a function that prints the multiplication table
(1 to 10) for a given number.
"""


# ---------------------------------------------------------------------
# CORE FUNCTION
# ---------------------------------------------------------------------

def print_multiplication_table(number: int) -> None:
    """
    Print the multiplication table for the given number.

    Args:
        number: Integer whose multiplication table is to be printed
    """
    for i in range(1, 11):
        print(f"{number} X {i} = {number * i}")


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    print_multiplication_table(5)


if __name__ == "__main__":
    main()
