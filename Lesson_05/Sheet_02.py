"""
dictionary_access_demo.py
------------------------

This script demonstrates dictionary operations in Python, particularly
the difference between:
- dict.get(key)
- dict[key]

It highlights how `get()` safely returns None when a key is missing,
while direct indexing raises a KeyError.
"""


# ---------------------------------------------------------------------
# CORE FUNCTION
# ---------------------------------------------------------------------

def demonstrate_dictionary_access(data: dict) -> None:
    """
    Demonstrate safe vs direct dictionary key access.

    Args:
        data: Dictionary containing sample key-value pairs
    """
    print("Using get():", data.get("Harry2"))  # Returns None if key does not exist

    try:
        print("Using direct indexing:", data["Harry2"])  # Raises KeyError
    except KeyError as exc:
        print("Direct indexing raised KeyError:", exc)


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    marks = {
        "Harry": 100,
        "Shubham": 56,
        "Rohan": 23,
        0: "Harry"
    }

    demonstrate_dictionary_access(marks)


if __name__ == "__main__":
    main()
