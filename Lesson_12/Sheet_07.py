from typing import List


def display_indexed_items(items: List[int]) -> None:
    """
    Display each element in the list along with its corresponding index
    using Python's built-in enumerate() function.

    Args:
        items (List[int]): A list of integer values.
    """
    for index, item in enumerate(items):
        print(f"The item at index {index} is {item}")


if __name__ == "__main__":
    values: List[int] = [3, 513, 53, 535]
    display_indexed_items(values)
