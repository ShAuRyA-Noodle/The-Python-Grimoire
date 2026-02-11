def format_message(name: str, descriptor: str) -> str:
    """
    Format a message using positional placeholders with the
    `str.format()` method.

    Args:
        name (str): Name to include in the message.
        descriptor (str): Descriptive word used in the message.

    Returns:
        str: Formatted output string.
    """
    return "{1} is a good {0}".format(name, descriptor)


if __name__ == "__main__":
    message = format_message("harry", "boy")
    print(message)
