from functools import reduce
from typing import List


def compute_squares(values: List[int]) -> List[int]:
    """
    Compute the square of each number using the map function.

    Args:
        values (List[int]): Input list of integers.

    Returns:
        List[int]: List containing squared values.
    """
    return list(map(lambda x: x * x, values))


def filter_even_numbers(values: List[int]) -> List[int]:
    """
    Filter even numbers from a list using the filter function.

    Args:
        values (List[int]): Input list of integers.

    Returns:
        List[int]: List containing only even numbers.
    """
    return list(filter(lambda n: n % 2 == 0, values))


def compute_sum(values: List[int]) -> int:
    """
    Compute the sum of elements using reduce.

    Args:
        values (List[int]): Input list of integers.

    Returns:
        int: Sum of elements.
    """
    return reduce(lambda a, b: a + b, values)


def compute_product(values: List[int]) -> int:
    """
    Compute the product of elements using reduce.

    Args:
        values (List[int]): Input list of integers.

    Returns:
        int: Product of elements.
    """
    return reduce(lambda a, b: a * b, values)


if __name__ == "__main__":
    numbers: List[int] = [1, 2, 3, 4, 5]

    print("Squares:", compute_squares(numbers))
    print("Even numbers:", filter_even_numbers(numbers))
    print("Sum:", compute_sum(numbers))
    print("Product:", compute_product(numbers))
