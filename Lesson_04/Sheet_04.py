"""
list_methods_demo.py
--------------------

This script demonstrates common list operations in Python, including:
- Appending elements
- Sorting and reversing (commented examples)
- Inserting elements
- Removing elements using pop()

Lists are mutable sequences widely used for dynamic collections of data.
"""


# ---------------------------------------------------------------------
# CORE FUNCTIONS
# ---------------------------------------------------------------------

def demonstrate_append_operation(items: list) -> None:
    """
    Append a new element to a list and display the result.

    Args:
        items: List to modify
    """
    print(f"Original list: {items}")
    items.append("Harry")
    print(f"List after append(): {items}")


def demonstrate_pop_operation(numbers: list) -> None:
    """
    Remove an element from a list using pop() and display results.

    Args:
        numbers: List of numeric values
    """
    popped_value = numbers.pop(3)
    print(f"Value removed using pop(): {popped_value}")
    print(f"List after pop(): {numbers}")


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    friends = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]
    demonstrate_append_operation(friends)

    l1 = [1, 34, 62, 2, 6, 11]
    demonstrate_pop_operation(l1)


if __name__ == "__main__":
    main()
