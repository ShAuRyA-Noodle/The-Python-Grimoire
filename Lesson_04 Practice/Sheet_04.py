"""
tuple_immutability_demo.py
--------------------------

This script demonstrates tuple immutability in Python. Tuples cannot be
modified after creation, meaning individual elements cannot be reassigned.

Attempting to change a tuple element results in a TypeError.
"""


# ---------------------------------------------------------------------
# DEMONSTRATION
# ---------------------------------------------------------------------

def demonstrate_tuple_immutability():
    """
    Attempt to modify a tuple element (will raise an error).
    """
    a = (34, 234, "Harry")

    try:
        a[2] = "Larry"   # This operation is not allowed
    except TypeError as exc:
        print("Error:", exc)

    print("Original tuple remains unchanged:", a)


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    demonstrate_tuple_immutability()


if __name__ == "__main__":
    main()
