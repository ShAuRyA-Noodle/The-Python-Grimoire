"""
age_and_parity_check.py
-----------------------

This script performs two checks based on user input:
1. Determines whether the entered number (age) is even or odd.
2. Determines whether the user is above or below the age of consent.

It demonstrates conditional branching, modular functions, and input validation.
"""


# ---------------------------------------------------------------------
# CORE FUNCTIONS
# ---------------------------------------------------------------------

def check_parity(number: int) -> str:
    """
    Determine whether a number is even or odd.

    Args:
        number: Integer value

    Returns:
        Parity message
    """
    return "The number is even." if number % 2 == 0 else "The number is odd."


def check_age_status(age: int) -> str:
    """
    Determine the age status of the user.

    Args:
        age: User's age

    Returns:
        Age status message
    """
    if age < 0:
        return "Invalid input: Age cannot be negative."
    elif age >= 18:
        return "You are above the age of consent. Good for you."
    else:
        return "You are below the age of consent."


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    try:
        age = int(input("Enter your age: "))

        print(check_parity(age))
        print(check_age_status(age))

    except ValueError:
        print("Invalid input. Please enter a valid integer.")

    print("End of Program")


if __name__ == "__main__":
    main()
