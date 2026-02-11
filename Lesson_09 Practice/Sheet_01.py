"""
file_keyword_search.py
----------------------

This script reads a file and checks whether a specific keyword is
present in the file content using a case-insensitive search.
"""


# ---------------------------------------------------------------------
# CORE FUNCTION
# ---------------------------------------------------------------------

def contains_keyword(filepath: str, keyword: str) -> bool:
    """
    Check whether a keyword exists in a file.

    Args:
        filepath: Path to the file
        keyword: Word to search for

    Returns:
        True if keyword exists, otherwise False
    """
    with open(filepath, "r") as file:
        content = file.read()
        return keyword.lower() in content.lower()


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    if contains_keyword("log.txt", "python"):
        print("Yes, 'python' is present.")
    else:
        print("No, 'python' is not present.")


if __name__ == "__main__":
    main()
