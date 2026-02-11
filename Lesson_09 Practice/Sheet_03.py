"""
file_copy.py
------------

This script copies the contents of one file to another file using
Python's context-manager approach for safe file handling.
"""


# ---------------------------------------------------------------------
# CORE FUNCTION
# ---------------------------------------------------------------------

def copy_file(source_path: str, destination_path: str) -> None:
    """
    Copy contents from one file to another.

    Args:
        source_path: Path of the source file
        destination_path: Path of the destination file
    """
    with open(source_path, "r") as src:
        content = src.read()

    with open(destination_path, "w") as dest:
        dest.write(content)


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    copy_file("this.txt", "this_copy.txt")


if __name__ == "__main__":
    main()
