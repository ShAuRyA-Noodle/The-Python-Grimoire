"""
age_check.py
------------

This script checks whether a user is above or below the age of consent
based on the entered age. It demonstrates conditional statements,
input validation, and formatted output.

Typical use cases:
- Eligibility checks
- Form validation systems
- Access control logic
"""


# ---------------------------------------------------------------------
# CORE FUNCTION
# ---------------------------------------------------------------------

def check_age_eligibility(age: int) -> str:
    """
    Determine whether the user is above the age of consent.

    Args:
        age: User's age

    Returns:
        Eligibility message
    """
    if age >= 18:
        return "You are above the age of consent. Good for you."
    else:
        return "You are below the age of consent."


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    try:
        age = int(input("Enter your age: "))
        message = check_age_eligibility(age)
        print(message)
    except ValueError:
        print("Invalid input. Please enter a valid numeric age.")

    print("End of Program")


if __name__ == "__main__":
    main()
