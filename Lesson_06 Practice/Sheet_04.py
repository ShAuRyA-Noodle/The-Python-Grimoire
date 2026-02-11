"""
username_length_checker.py
--------------------------

This script checks whether a username contains fewer than 10 characters.
It demonstrates string length validation and conditional branching.

Typical use cases:
- Username validation systems
- Form input validation
- Registration rule enforcement
"""


# ---------------------------------------------------------------------
# CORE FUNCTION
# ---------------------------------------------------------------------

def is_username_short(username: str, limit: int = 10) -> bool:
    """
    Determine whether the username length is less than the specified limit.

    Args:
        username: Input username
        limit: Maximum allowed length threshold

    Returns:
        True if username length is less than limit, otherwise False
    """
    return len(username) < limit


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    username = input("Enter username: ").strip()

    if is_username_short(username):
        print("Your username contains fewer than 10 characters.")
    else:
        print("Your username contains 10 or more characters.")


if __name__ == "__main__":
    main()
