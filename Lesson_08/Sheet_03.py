"""
average_calculator.py
---------------------

This script demonstrates how to calculate the average of three numbers
using a reusable function. It separates input collection from the
calculation logic, which improves reusability and testability.
"""


# ---------------------------------------------------------------------
# CORE FUNCTION
# ---------------------------------------------------------------------

def calculate_average(a: int, b: int, c: int) -> float:
    """
    Calculate the average of three numbers.

    Args:
        a: First number
        b: Second number
        c: Third number

    Returns:
        Average value
    """
    return (a + b + c) / 3


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    try:
        for _ in range(5):
            a = int(input("Enter number 1: "))
            b = int(input("Enter number 2: "))
            c = int(input("Enter number 3: "))

            avg = calculate_average(a, b, c)
            print(f"Average: {avg}")
            print("Thank you!")

    except ValueError:
        print("Invalid input. Please enter valid integers.")


if __name__ == "__main__":
    main()
