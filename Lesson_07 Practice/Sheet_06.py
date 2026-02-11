"""
name_greeting_filter.py
-----------------------

This script filters names that start with a specific letter and prints
a greeting for those names. It demonstrates string prefix checking and
iteration over lists.

Typical use cases:
- Contact filtering systems
- Notification targeting
- Dataset filtering operations
"""


# ---------------------------------------------------------------------
# CORE FUNCTION
# ---------------------------------------------------------------------

def greet_names_starting_with(names: list, letter: str) -> None:
    """
    Print greetings for names starting with a specific letter.

    Args:
        names: List of names
        letter: Starting letter to filter names
    """
    for name in names:
        if name.startswith(letter):
            print(f"Hello {name}")


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    names_list = ["Harry", "Soham", "Sachin", "Rahul"]
    greet_names_starting_with(names_list, "S")


if __name__ == "__main__":
    main()
