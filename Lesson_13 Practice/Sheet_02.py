from typing import List


def generate_table_lines(number: int, limit: int = 10) -> List[str]:
    """
    Generate formatted multiplication table lines for a given number.

    Args:
        number (int): The number for which the multiplication table is generated.
        limit (int): The number of multiples to generate (default is 10).

    Returns:
        List[str]: A list of formatted multiplication results as strings.
    """
    return [str(number * i) for i in range(1, limit + 1)]


def print_table(number: int) -> None:
    """
    Print the multiplication table of a number line by line.

    Args:
        number (int): The number whose multiplication table will be printed.
    """
    lines = generate_table_lines(number)
    output = "\n".join(lines)
    print(output)


if __name__ == "__main__":
    print_table(7)
