"""
file_multiword_censor.py
------------------------

This script replaces multiple offensive words in a text file with
masked characters (e.g., ####). It performs case-insensitive matching
and writes the updated content back to the file.
"""

import re


# ---------------------------------------------------------------------
# CORE FUNCTION
# ---------------------------------------------------------------------

def censor_words(filepath: str, words: list) -> None:
    """
    Replace given words in a file with masked characters.

    Args:
        filepath: Path to the file
        words: List of words to censor
    """
    with open(filepath, "r") as file:
        content = file.read()

    for word in words:
        pattern = re.compile(re.escape(word), re.IGNORECASE)
        content = pattern.sub("#" * len(word), content)

    with open(filepath, "w") as file:
        file.write(content)


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    words_to_censor = ["Donkey", "bad", "ganda"]
    censor_words("file.txt", words_to_censor)


if __name__ == "__main__":
    main()
