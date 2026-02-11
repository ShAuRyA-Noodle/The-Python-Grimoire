"""
list_word_removal.py
--------------------

Remove all occurrences of a specific word from a list and return the
filtered list.
"""


# ---------------------------------------------------------------------
# CORE FUNCTION
# ---------------------------------------------------------------------

def remove_word(items: list, word: str) -> list:
    """
    Remove all occurrences of a given word from a list.

    Args:
        items: List of strings
        word: Word to remove

    Returns:
        New list with the word removed
    """
    result = []
    for item in items:
        if item != word:
            result.append(item)
    return result


# ---------------------------------------------------------------------
# EXAMPLE USAGE
# ---------------------------------------------------------------------

l = ["Harry", "Rohan", "Shubham", "an"]

print(remove_word(l, "an"))
