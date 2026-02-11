"""
list_mutability_demo.py
-----------------------

This script demonstrates key properties of Python lists:
- Accessing elements by index
- Modifying elements (lists are mutable)
- Slicing a list to retrieve sublists

Lists are mutable sequences commonly used for storing collections of
heterogeneous or homogeneous data.
"""


# ---------------------------------------------------------------------
# CORE FUNCTION
# ---------------------------------------------------------------------

def demonstrate_list_operations(items: list) -> None:
    """
    Demonstrate indexing, modification, and slicing of a list.

    Args:
        items: List containing sample elements
    """
    print(f"Original first element: {items[0]}")

    # Modify first element (lists are mutable)
    items[0] = "Grapes"
    print(f"Modified first element: {items[0]}")

    # Slice elements from index 1 to 4 (excluding index 4)
    sliced_items = items[1:4]
    print(f"Sliced list (1:4): {sliced_items}")


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    friends = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]
    demonstrate_list_operations(friends)


if __name__ == "__main__":
    main()
