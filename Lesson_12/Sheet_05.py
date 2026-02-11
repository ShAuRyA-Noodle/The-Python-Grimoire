from typing import List, Union, Tuple


# Typed variable declarations
count: int = 5
name: str = "Harry"


def add_numbers(a: int, b: int) -> int:
    """
    Compute the sum of two integers.

    Args:
        a (int): First integer value.
        b (int): Second integer value.

    Returns:
        int: The result of adding the two integers.
    """
    return a + b


if __name__ == "__main__":
    result = add_numbers(3, 4)
    print(f"Result: {result}")
