"""
set_creation_demo.py
-------------------

This script demonstrates how to correctly create sets in Python and
explains the difference between:
- {}   → creates an empty dictionary
- set() → creates an empty set

It also shows that sets automatically remove duplicate values.
"""


# ---------------------------------------------------------------------
# CORE FUNCTION
# ---------------------------------------------------------------------

def demonstrate_set_creation() -> None:
    """
    Create sets and display their contents.
    """
    empty_set = set()   # Correct way to create an empty set
    sample_set = {1, 5, 32, 54, 5, 5, 5}  # Duplicate values are removed automatically

    print(f"Empty set: {empty_set}, Type: {type(empty_set)}")
    print(f"Sample set (duplicates removed): {sample_set}")


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    demonstrate_set_creation()


if __name__ == "__main__":
    main()
