"""
tuple_operations_demo.py
-----------------------

This script demonstrates common tuple operations in Python, including:
- Counting occurrences of a value
- Finding the index of an element
- Determining tuple length

Tuples are immutable sequences often used to store fixed collections
of related values.
"""


# ---------------------------------------------------------------------
# CORE FUNCTION
# ---------------------------------------------------------------------

def demonstrate_tuple_operations(data: tuple) -> None:
    """
    Display results of various tuple operations.

    Args:
        data: Tuple containing sample values
    """
    print(f"Tuple contents: {data}")

    count_45 = data.count(45)
    print(f"Number of occurrences of 45: {count_45}")

    index_3424 = data.index(3424)
    print(f"Index of value 3424: {index_3424}")

    length = len(data)
    print(f"Length of tuple: {length}")


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    a = (1, 45, 342, 3424, False, 45, "Rohan", "Shivam")
    demonstrate_tuple_operations(a)


if __name__ == "__main__":
    main()
