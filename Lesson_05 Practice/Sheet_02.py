"""
friends_language_mapping.py
---------------------------

This script collects names of friends and their preferred programming
languages, stores them in a dictionary, and displays the final mapping.

It demonstrates:
- Dictionary updates
- Loop-based input collection
- Dynamic key-value storage
"""


# ---------------------------------------------------------------------
# CORE FUNCTION
# ---------------------------------------------------------------------

def collect_friend_languages(count: int) -> dict:
    """
    Collect friend names and their preferred languages.

    Args:
        count: Number of entries to collect

    Returns:
        Dictionary mapping friend names to languages
    """
    data = {}

    for i in range(count):
        name = input(f"Enter friend's name {i + 1}: ")
        language = input(f"Enter {name}'s preferred language: ")
        data[name] = language

    return data


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    friends_languages = collect_friend_languages(4)
    print("Friend-Language Mapping:", friends_languages)


if __name__ == "__main__":
    main()
