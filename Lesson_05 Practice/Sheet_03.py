"""
unique_numbers_collector.py
---------------------------

This script collects multiple numeric inputs from the user and stores
them in a set. Because sets automatically remove duplicates, the final
output contains only unique values.

It demonstrates:
- Set operations
- Loop-based input collection
- Input validation
"""


# ---------------------------------------------------------------------
# CORE FUNCTION
# ---------------------------------------------------------------------

def collect_unique_numbers(count: int) -> set:
    """
    Collect a specified number of integers and store them in a set.

    Args:
        count: Number of inputs to collect

    Returns:
        Set containing unique entered integers
    """
    numbers = set()

    for i in range(count):
        while True:
            try:
                value = int(input(f"Enter number {i + 1}: "))
                numbers.add(value)
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

    return numbers


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    unique_numbers = collect_unique_numbers(8)
    print("Unique numbers entered:", unique_numbers)


if __name__ == "__main__":
    main()
