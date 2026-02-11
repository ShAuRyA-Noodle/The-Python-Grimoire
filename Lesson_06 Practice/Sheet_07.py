"""
spam_detector.py
----------------

This script checks whether a given message contains common spam phrases.
It demonstrates keyword-based filtering and scalable pattern matching.

Typical use cases:
- Comment moderation systems
- Email spam filters (basic rule-based)
- Content screening pipelines
"""


# ---------------------------------------------------------------------
# CORE FUNCTION
# ---------------------------------------------------------------------

def is_spam(message: str, spam_phrases: list) -> bool:
    """
    Determine whether a message contains any spam phrase.

    Args:
        message: Input text message
        spam_phrases: List of phrases considered spam

    Returns:
        True if message contains spam phrase, otherwise False
    """
    message_lower = message.lower()
    return any(phrase.lower() in message_lower for phrase in spam_phrases)


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    spam_phrases = [
        "make a lot of money",
        "buy now",
        "subscribe this",
        "click this"
    ]

    message = input("Enter your comment: ").strip()

    if is_spam(message, spam_phrases):
        print("This comment is spam.")
    else:
        print("This comment is not spam.")


if __name__ == "__main__":
    main()
