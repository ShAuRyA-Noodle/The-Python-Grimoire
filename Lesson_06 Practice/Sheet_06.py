"""
name_membership_check.py
------------------------

This script checks whether a user's name exists in a predefined list.
It demonstrates membership testing in lists and input normalization.

Typical use cases:
- Access control lists
- Registration verification
- Membership validation systems
"""


# ---------------------------------------------------------------------
# CORE FUNCTION
# ---------------------------------------------------------------------

def is_name_in_list(name: str, name_list: list) -> bool:
    """
    Check whether a name exists in a list (case-insensitive).

    Args:
        name: Name entered by the user
        name_list: List of valid names

    Returns:
        True if the name exists in the list, otherwise False
    """
    return name.lower() in (n.lower() for n in name_list)


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    names = ["Harry", "Rohan", "Shubham", "Divya"]
    user_name = input("Enter your name: ").strip()

    if is_name_in_list(user_name, names):
        print("Your name is in the list.")
    else:
        print("Your name is not in the list.")


if __name__ == "__main__":
    main()
