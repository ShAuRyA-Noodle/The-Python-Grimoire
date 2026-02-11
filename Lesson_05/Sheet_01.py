"""
set_operations_demo.py
---------------------

This script demonstrates basic operations on Python sets, including:
- Automatic removal of duplicate elements
- Adding elements using add()
- Removing elements using remove()

Sets are unordered collections of unique elements commonly used for
membership testing and eliminating duplicates.
"""


# ---------------------------------------------------------------------
# CORE FUNCTION
# ---------------------------------------------------------------------

def demonstrate_set_operations(data: set) -> None:
    """
    Perform basic set operations and display results.

    Args:
        data: Initial set of elements
    """
    print(f"Initial set: {data}, Type: {type(data)}")

    # Add a new element
    data.add(566)
    print(f"After add(566): {data}")

    # Remove an element
    data.remove(1)
    print(f"After remove(1): {data}")


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    s = {1, 5, 32, 54, 5, 5, 5, "Harry"}  # Duplicate values are automatically removed
    demonstrate_set_operations(s)


if __name__ == "__main__":
    main()
