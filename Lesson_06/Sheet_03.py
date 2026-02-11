"""
age_validation.py
-----------------

This script validates the user's age and determines whether the user
is above or below the age of consent. It demonstrates proper ordering
of conditional checks and input validation.

Key concept:
Always validate invalid inputs (negative or zero values) before
processing business logic.
"""


# ---------------------------------------------------------------------
# CORE FUNCTION
# ---------------------------------------------------------------------

def evaluate_age(age: int) -> str:
    """
    Evaluate the user's age and return an appropriate message.

    Args:
        age: User-entered age

    Returns:
        Status message based on age
    """
    if age < 0:
        return "Invalid input: Age cannot be negative."
    elif age == 0:
        return "Age cannot be zero. Please enter a valid age."
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
        message = evaluate_age(age)
        print(message)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

    print("End of Program")


if __name__ == "__main__":
    main()
