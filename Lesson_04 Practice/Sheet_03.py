"""
tuple_count_demo.py
------------------

This script demonstrates how to count the number of occurrences of a
specific value in a tuple using the built-in `count()` method.

Typical use cases:
- Data validation checks
- Frequency analysis
- Detecting missing or placeholder values
"""


# ---------------------------------------------------------------------
# CORE FUNCTION
# ---------------------------------------------------------------------

def count_value(data: tuple, value) -> int:
    """
    Count how many times a value appears in a tuple.

    Args:
        data: Tuple containing elements
        value: Value whose occurrences are to be counted

    Returns:
        Number of occurrences of the value
    """
    return data.count(value)


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    a = (7, 0, 8, 0, 0, 9)
    zero_count = count_value(a, 0)

    print(f"Tuple: {a}")
    print(f"Number of occurrences of 0: {zero_count}")


if __name__ == "__main__":
    main()
