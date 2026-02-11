"""
file_word_censor.py
-------------------

This script replaces a specified word in a text file with a masked value
(e.g., "######") and writes the updated content back to the same file.
"""


# ---------------------------------------------------------------------
# CORE FUNCTION
# ---------------------------------------------------------------------

def censor_word(filepath: str, word: str, replacement: str = "######") -> None:
    """
    Replace all occurrences of a word in a file with a replacement string.

    Args:
        filepath: Path to the file
        word: Word to be censored
        replacement: Replacement text (default: "######")
    """
    with open(filepath, "r") as file:
        content = file.read()

    updated_content = content.replace(word, replacement)

    with open(filepath, "w") as file:
        file.write(updated_content)


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    censor_word("file.txt", "Donkey")


if __name__ == "__main__":
    main()
