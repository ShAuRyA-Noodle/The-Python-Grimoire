from typing import List


def print_selected_items(values: List[int], indices: List[int]) -> None:
    """
    Print elements from a list that correspond to specific indices.

    Args:
        values (List[int]): The list containing elements.
        indices (List[int]): Indices whose elements should be printed.
    """
    selected_indices = set(indices)  # Improves lookup performance

    for index, item in enumerate(values):
        if index in selected_indices:
            print(item)


if __name__ == "__main__":
    numbers: List[int] = [1, 2, 3, 4, 5, 6, 7, 8]
    target_indices: List[int] = [2, 4, 6]

    print_selected_items(numbers, target_indices)
