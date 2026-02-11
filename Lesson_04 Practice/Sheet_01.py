"""
marks_collector.py
------------------

This script collects multiple student marks from user input, stores them
in a list, sorts the list in ascending order, and displays the result.

It demonstrates:
- List operations
- Loops for repeated input collection
- Input validation
- Sorting lists
"""


# ---------------------------------------------------------------------
# CORE FUNCTIONS
# ---------------------------------------------------------------------

def collect_marks(count: int) -> list:
    """
    Collect a specified number of marks from user input.

    Args:
        count: Number of marks to collect

    Returns:
        List containing collected marks
    """
    marks = []

    for i in range(count):
        while True:
            try:
                value = int(input(f"Enter mark {i + 1}: "))
                marks.append(value)
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

    return marks


def sort_marks(marks: list) -> list:
    """
    Sort the marks list in ascending order.

    Args:
        marks: List of marks

    Returns:
        Sorted list of marks
    """
    return sorted(marks)


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    marks = collect_marks(6)
    sorted_marks = sort_marks(marks)

    print("Sorted marks:", sorted_marks)


if __name__ == "__main__":
    main()
