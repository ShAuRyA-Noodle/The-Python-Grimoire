"""
tuple_type_demo.py
------------------

This script demonstrates how to create a tuple in Python and determine
its data type using the built-in `type()` function.

Tuples are immutable sequences often used to store fixed collections
of related values.
"""


# ---------------------------------------------------------------------
# CORE FUNCTION
# ---------------------------------------------------------------------

def display_tuple_info(data: tuple) -> None:
    """
    Print the tuple contents and its data type.

    Args:
        data: Tuple to inspect
    """
    print(f"Tuple contents: {data}")
    print(f"Data type: {type(data)}")


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    a = (1, 45, 342, 3424, False, "Rohan", "Shivam")
    display_tuple_info(a)


if __name__ == "__main__":
    main()
