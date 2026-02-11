"""
keyword_check_in_file.py
------------------------

This script checks whether a specific word exists in a file.
It uses a context manager (`with open`) to ensure the file is
automatically closed after reading.
"""


# ---------------------------------------------------------------------
# KEYWORD CHECK
# ---------------------------------------------------------------------

def contains_word(filepath: str, word: str) -> bool:
    """
    Check whether a word exists in a file (case-insensitive).

    Args:
        filepath: Path to the file
        word: Word to search for

    Returns:
        True if the word exists, otherwise False
    """
    with open(filepath, "r") as file:
        content = file.read()
        return word.lower() in content.lower()


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    if contains_word("poem.txt", "twinkle"):
        print("The word 'twinkle' is present in the content.")
    else:
        print("The word 'twinkle' is not present in the content.")


if __name__ == "__main__":
    main()
