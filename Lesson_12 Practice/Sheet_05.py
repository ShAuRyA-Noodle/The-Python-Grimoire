from typing import List


def generate_multiplication_table(number: int) -> List[int]:
    """
    Generate the multiplication table (1–10) for a given number.

    Args:
        number (int): The number for which the table is generated.

    Returns:
        List[int]: A list containing multiplication results.
    """
    return [number * i for i in range(1, 11)]


def save_table_to_file(number: int, file_path: str = "tables.txt") -> None:
    """
    Generate the multiplication table and append it to a file.

    Args:
        number (int): The number whose multiplication table will be saved.
        file_path (str): Path of the file where the table will be stored.
    """
    table = generate_multiplication_table(number)

    with open(file_path, "a", encoding="utf-8") as file:
        file.write(f"Table of {number}: {table}\n")


def main() -> None:
    """
    Prompt the user for a number and save its multiplication table to a file.
    """
    try:
        number = int(input("Enter a number: "))
        save_table_to_file(number)
        print("Multiplication table successfully saved.")

    except ValueError:
        print("Invalid input. Please enter a valid integer.")


if __name__ == "__main__":
    main()
