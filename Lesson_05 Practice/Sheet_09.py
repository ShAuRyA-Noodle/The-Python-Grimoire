"""
dictionary_lookup.py
--------------------

This script stores a small bilingual dictionary and allows the user to
enter a word to retrieve its meaning. It demonstrates dictionary lookup,
user input handling, and safe access using `get()` to avoid runtime errors.
"""


# ---------------------------------------------------------------------
# CORE FUNCTION
# ---------------------------------------------------------------------

def get_word_meaning(dictionary: dict, word: str) -> str:
    """
    Retrieve the meaning of a word from the dictionary.

    Args:
        dictionary: Mapping of words to meanings
        word: Word whose meaning is requested

    Returns:
        Meaning of the word if found, otherwise a fallback message
    """
    return dictionary.get(word, "Meaning not found in dictionary.")


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    words = {
        "madad": "Help",
        "kursi": "Chair",
        "billi": "Cat"
    }

    user_word = input("Enter the word you want meaning of: ").strip().lower()
    meaning = get_word_meaning(words, user_word)

    print(f"Meaning: {meaning}")


if __name__ == "__main__":
    main()
