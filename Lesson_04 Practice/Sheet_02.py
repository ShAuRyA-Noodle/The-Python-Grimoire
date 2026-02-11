"""
list_sum_demo.py
----------------

This script demonstrates how to calculate the sum of numeric elements
in a list using Python's built-in `sum()` function.

Common use cases:
- Calculating totals in datasets
- Aggregating numeric values
- Data analysis preprocessing
"""


# ---------------------------------------------------------------------
# CORE FUNCTION
# ---------------------------------------------------------------------

def calculate_list_sum(numbers: list) -> int:
    """
    Calculate the sum of all elements in a list.

    Args:
        numbers: List containing numeric values

    Returns:
        Sum of the list elements
    """
    return sum(numbers)


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    l = [3, 3, 5, 1]
    total = calculate_list_sum(l)

    print(f"List: {l}")
    print(f"Sum of elements: {total}")


if __name__ == "__main__":
    main()
