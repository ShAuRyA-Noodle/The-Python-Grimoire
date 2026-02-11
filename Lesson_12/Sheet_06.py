from typing import List


def compute_squared_values(values: List[int]) -> List[int]:
    """
    Compute the square of each element in a list of integers.

    Args:
        values (List[int]): A list containing integer values.

    Returns:
        List[int]: A new list containing the squared values.
    """
    return [value * value for value in values]


if __name__ == "__main__":
    numbers: List[int] = [1, 2, 9, 5, 3, 5]

    squared_numbers = compute_squared_values(numbers)
    print(squared_numbers)
