"""
file_line_reader.py
-------------------

This script reads a text file line-by-line and prints each line.
It demonstrates the preferred iteration method for reading files
efficiently.
"""


# ---------------------------------------------------------------------
# FILE READING LINE BY LINE
# ---------------------------------------------------------------------

def read_file_lines(filepath: str) -> None:
    """
    Read and print file contents line by line.

    Args:
        filepath: Path to the file
    """
    with open(filepath, "r") as file:
        for line in file:
            print(line, end="")


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    read_file_lines("file.txt")


if __name__ == "__main__":
    main()
