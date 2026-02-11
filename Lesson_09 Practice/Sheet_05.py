"""
multiplication_tables_generator.py
----------------------------------

This script generates multiplication tables (1–10) for numbers within a
specified range and saves each table as a separate text file inside the
`tables` directory.
"""

import os


# ---------------------------------------------------------------------
# CORE FUNCTION
# ---------------------------------------------------------------------

def generate_table(n: int, directory: str = "tables") -> None:
    """
    Generate the multiplication table of a number and save it to a file.

    Args:
        n: Number whose table will be generated
        directory: Folder where table files will be stored
    """
    os.makedirs(directory, exist_ok=True)  # Ensure directory exists

    table_content = ""
    for i in range(1, 11):
        table_content += f"{n} X {i} = {n * i}\n"

    file_path = os.path.join(directory, f"table_{n}.txt")
    with open(file_path, "w") as file:
        file.write(table_content)


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    for i in range(2, 21):
        generate_table(i)


if __name__ == "__main__":
    main()
