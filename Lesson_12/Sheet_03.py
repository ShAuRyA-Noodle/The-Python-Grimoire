def http_status(status: int) -> str:
    """
    Return a descriptive message corresponding to an HTTP status code
    using Python's structural pattern matching.

    Args:
        status (int): HTTP status code.

    Returns:
        str: A human-readable description of the status code.
    """
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            # Default case for any unspecified status codes
            return "Unknown status"


if __name__ == "__main__":
    print(http_status(5007))
