"""
file_comparison.py
------------------

This script compares the contents of two files and determines whether
they are identical.
"""


# ---------------------------------------------------------------------
# CORE FUNCTION
# ---------------------------------------------------------------------

def files_are_identical(file1: str, file2: str) -> bool:
    """
    Compare two files and check if their contents are identical.

    Args:
        file1: Path to first file
        file2: Path to second file

    Returns:
        True if files are identical, otherwise False
    """
    with open(file1, "r") as f1, open(file2, "r") as f2:
        return f1.read() == f2.read()


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    if files_are_identical("this.txt", "this_copy.txt"):
        print("Yes, these files are identical.")
    else:
        print("No, these files are not identical.")


if __name__ == "__main__":
    main()
