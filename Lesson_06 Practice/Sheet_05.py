"""
keyword_detection.py
--------------------

This script checks whether a given text post contains a specific keyword
("harry") in a case-insensitive manner. It demonstrates substring search,
string normalization, and conditional logic.

Typical use cases:
- Content moderation systems
- Keyword monitoring tools
- Social media text analysis
"""


# ---------------------------------------------------------------------
# CORE FUNCTION
# ---------------------------------------------------------------------

def contains_keyword(text: str, keyword: str) -> bool:
    """
    Determine whether a keyword exists in the given text (case-insensitive).

    Args:
        text: Input text to analyze
        keyword: Keyword to search for

    Returns:
        True if keyword exists in the text, otherwise False
    """
    return keyword.lower() in text.lower()


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    post = input("Enter the post: ").strip()

    if contains_keyword(post, "harry"):
        print("This post is talking about Harry.")
    else:
        print("This post is not talking about Harry.")


if __name__ == "__main__":
    main()
