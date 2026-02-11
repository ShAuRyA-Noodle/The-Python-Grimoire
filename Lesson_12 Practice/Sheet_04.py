from typing import List


def generate_multiplication_table(number: int) -> List[int]:
    """
    Generate the multiplication table (1–10) for a given number.

    Args:
        number (int): The number for which the multiplication table is generated.

    Returns:
        List[int]: A list containing the multiplication results.
    """
    return [number * i for i in range(1, 11)]


def main() -> None:
    """
    Prompt the user for a number and display its multiplication table.
    """
    try:
        user_input = int(input("Enter a number: "))
        table = generate_multiplication_table(user_input)
        print(table)

    except ValueError:
        print("Invalid input. Please enter a valid integer.")


if __name__ == "__main__":
    main()
