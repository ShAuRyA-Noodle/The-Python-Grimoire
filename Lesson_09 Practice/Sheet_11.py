"""
clear_file_content.py
---------------------

This script demonstrates how to clear the contents of a file safely
using Python's context manager.
"""


# ---------------------------------------------------------------------
# CORE FUNCTION
# ---------------------------------------------------------------------

def clear_file(filepath: str) -> None:
    """
    Clear all content from a file.

    Args:
        filepath: Path to the file to be cleared
    """
    with open(filepath, "w") as file:
        file.write("")  # Writing an empty string clears the file


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    clear_file("this_copy.txt")
    print("File content cleared successfully.")


if __name__ == "__main__":
    main()
