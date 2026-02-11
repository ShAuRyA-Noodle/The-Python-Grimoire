"""
file_write_example.py
---------------------

This script writes a string to a text file. It demonstrates safe file
handling using the `with open()` context manager, which automatically
closes the file after writing.
"""


# ---------------------------------------------------------------------
# FILE WRITING
# ---------------------------------------------------------------------

def write_to_file(filepath: str, content: str) -> None:
    """
    Write content to a file.

    Args:
        filepath: Path to the file
        content: Text content to write
    """
    with open(filepath, "w") as file:
        file.write(content)


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    text = "Hey Harry you are amazing"
    write_to_file("myfile.txt", text)


if __name__ == "__main__":
    main()
