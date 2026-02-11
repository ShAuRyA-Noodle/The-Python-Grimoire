"""
multiplication_table.py
-----------------------

This script prints the multiplication table (1 to 10) of a number
entered by the user using a while loop. It demonstrates loop-controlled
iteration and formatted output using f-strings.
"""


# ---------------------------------------------------------------------
# CORE FUNCTION
# ---------------------------------------------------------------------

def print_table(number: int) -> None:
    """
    Print the multiplication table for the given number.

    Args:
        number: Integer whose multiplication table is to be printed
    """
    i = 1
    while i <= 10:
        print(f"{number} X {i} = {number * i}")
        i += 1


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    try:
        n = int(input("Enter a number: "))
        print_table(n)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")


if __name__ == "__main__":
    main()
