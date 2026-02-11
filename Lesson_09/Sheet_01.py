"""
file_read_example.py
--------------------

This script demonstrates how to read the contents of a text file in
Python. It uses the recommended context-manager (`with open`) approach,
which automatically closes the file after reading.
"""


# ---------------------------------------------------------------------
# FILE READING
# ---------------------------------------------------------------------

def read_file(filepath: str) -> str:
    """
    Read and return the contents of a file.

    Args:
        filepath: Path to the file

    Returns:
        File contents as a string
    """
    with open(filepath, "r") as file:
        return file.read()


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    data = read_file("file.txt")
    print(data)


if __name__ == "__main__":
    main()
