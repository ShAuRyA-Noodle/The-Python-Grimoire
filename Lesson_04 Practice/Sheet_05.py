"""
fruit_list_collector.py
-----------------------

This script collects multiple fruit names from user input and stores them
in a list. It demonstrates loop-based input collection and list operations.

Typical use cases:
- Collecting user-defined datasets
- CLI-based data entry tools
- Input-driven automation scripts
"""


# ---------------------------------------------------------------------
# CORE FUNCTION
# ---------------------------------------------------------------------

def collect_fruits(count: int) -> list:
    """
    Collect a specified number of fruit names from the user.

    Args:
        count: Number of fruit names to collect

    Returns:
        List containing the entered fruit names
    """
    fruits = []

    for i in range(count):
        fruit_name = input(f"Enter fruit name {i + 1}: ")
        fruits.append(fruit_name)

    return fruits


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    fruits = collect_fruits(7)
    print("Collected fruits:", fruits)


if __name__ == "__main__":
    main()
