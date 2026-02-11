"""
greeting_generator.py
---------------------

This script accepts a user's name as input and prints a personalized
greeting message using Python f-strings. It demonstrates basic input
handling and string formatting.

Typical use cases:
- CLI greeting utilities
- User onboarding messages
- Interactive scripts
"""


# ---------------------------------------------------------------------
# CORE FUNCTION
# ---------------------------------------------------------------------

def generate_greeting(name: str) -> str:
    """
    Generate a greeting message for the given name.

    Args:
        name: User's name

    Returns:
        Formatted greeting string
    """
    return f"Good Afternoon, {name}"


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    name = input("Enter your name: ")
    greeting = generate_greeting(name)

    print(greeting)


if __name__ == "__main__":
    main()
