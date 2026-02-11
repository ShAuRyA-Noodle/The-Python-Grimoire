"""
multiplication_table_for_loop.py
--------------------------------

This script prints the multiplication table (1 to 10) for a user-entered
number using a `for` loop and formatted string output.
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
    try:
        n = int(input("Enter a number: "))
        print_multiplication_table(n)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")


if __name__ == "__main__":
    main()
