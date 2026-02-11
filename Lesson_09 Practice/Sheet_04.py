"""
file_keyword_line_search.py
---------------------------

This script searches for a keyword in a file and prints the line number
where it first appears. It reads the file line-by-line for better
memory efficiency.
"""


# ---------------------------------------------------------------------
# KEYWORD SEARCH FUNCTION
# ---------------------------------------------------------------------

def find_keyword(filepath: str, keyword: str) -> None:
    """
    Search for a keyword in a file and print the line number.

    Args:
        filepath: Path to the file
        keyword: Word to search for
    """
    with open(filepath, "r") as file:
        for lineno, line in enumerate(file, start=1):
            if keyword.lower() in line.lower():
                print(f"Yes, '{keyword}' is present. Line no: {lineno}")
                break
        else:
            print(f"No '{keyword}' found in the file.")


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    find_keyword("log.txt", "python")


if __name__ == "__main__":
    main()
