"""
reverse_multiplication_table.py
-------------------------------

This script prints the multiplication table of a given number in
reverse order (from 10 down to 1). It demonstrates loop iteration,
formatted output using f-strings, and input handling.
"""


# ---------------------------------------------------------------------
# CORE FUNCTION
# ---------------------------------------------------------------------

def print_reverse_table(number: int) -> None:
    """
    Print the multiplication table of a number in reverse order.

    Args:
        number: Integer whose multiplication table is to be printed
    """
    for i in range(10, 0, -1):
        print(f"{number} X {i} = {number * i}")


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    try:
        n = int(input("Enter the number: "))
        print_reverse_table(n)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")


if __name__ == "__main__":
    main()
