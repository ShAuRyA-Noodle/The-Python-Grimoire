from typing import Callable


# Lambda function assigned to a variable for simple one-line operations
square: Callable[[int], int] = lambda x: x * x


def main() -> None:
    """
    Demonstrate the use of a lambda function to compute the square
    of a number.
    """
    result = square(5)
    print(result)


if __name__ == "__main__":
    main()
