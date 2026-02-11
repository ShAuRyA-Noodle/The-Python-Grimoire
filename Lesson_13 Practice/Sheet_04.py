from functools import reduce
from typing import List


def find_maximum(values: List[int]) -> int:
    """
    Find the maximum value in a list using functools.reduce().

    Args:
        values (List[int]): A list of integers.

    Returns:
        int: The maximum value in the list.
    """
    def greater(a: int, b: int) -> int:
        """Return the greater of two numbers."""
        return a if a > b else b

    return reduce(greater, values)


if __name__ == "__main__":
    numbers: List[int] = [111, 2, 65, 5553, 635, 65, 74, 45, 55]

    maximum_value = find_maximum(numbers)
    print(maximum_value)
