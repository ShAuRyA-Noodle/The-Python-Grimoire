from typing import List


def is_divisible_by_five(number: int) -> bool:
    """
    Check whether a number is divisible by 5.

    Args:
        number (int): The integer to evaluate.

    Returns:
        bool: True if the number is divisible by 5, otherwise False.
    """
    return number % 5 == 0


def filter_divisible_numbers(values: List[int]) -> List[int]:
    """
    Filter numbers divisible by 5 from a list of integers.

    Args:
        values (List[int]): Input list of integers.

    Returns:
        List[int]: List containing numbers divisible by 5.
    """
    return list(filter(is_divisible_by_five, values))


if __name__ == "__main__":
    numbers: List[int] = [1, 2, 34234, 53, 6234235, 64343, 65, 754, 45, 55]

    divisible_numbers = filter_divisible_numbers(numbers)
    print(divisible_numbers)
