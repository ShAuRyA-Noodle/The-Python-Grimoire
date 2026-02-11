"""
greatest_number_finder.py
-------------------------

This script accepts four numeric inputs from the user and determines
the greatest number among them. It demonstrates input handling,
list usage, and the built-in `max()` function for efficient comparison.
"""


# ---------------------------------------------------------------------
# CORE FUNCTION
# ---------------------------------------------------------------------

def find_greatest(numbers: list) -> int:
    """
    Return the greatest number from a list of numbers.

    Args:
        numbers: List containing numeric values

    Returns:
        The maximum number in the list
    """
    return max(numbers)


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    try:
        numbers = [
            int(input("Enter number 1: ")),
            int(input("Enter number 2: ")),
            int(input("Enter number 3: ")),
            int(input("Enter number 4: "))
        ]

        greatest = find_greatest(numbers)
        print(f"The greatest number is: {greatest}")

    except ValueError:
        print("Invalid input. Please enter valid integers.")


if __name__ == "__main__":
    main()
