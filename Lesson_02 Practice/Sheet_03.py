"""
average_calculator.py
---------------------

This script accepts two integer inputs from the user and calculates their
average. It demonstrates user input handling, arithmetic operations,
type conversion, and formatted output.
"""


# ---------------------------------------------------------------------
# CORE FUNCTION
# ---------------------------------------------------------------------

def calculate_average(a: float, b: float) -> float:
    """
    Calculate the average of two numbers.

    Args:
        a: First numeric value
        b: Second numeric value

    Returns:
        The average of the two numbers
    """
    return (a + b) / 2


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    try:
        a = float(input("Enter number 1: "))
        b = float(input("Enter number 2: "))

        avg = calculate_average(a, b)
        print(f"The average of these two numbers is: {avg}")

    except ValueError:
        print("Invalid input. Please enter valid numeric values.")


if __name__ == "__main__":
    main()
