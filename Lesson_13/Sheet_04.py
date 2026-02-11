from typing import List


def join_names(names: List[str], separator: str = "::") -> str:
    """
    Join a list of strings into a single string using a specified separator.

    Args:
        names (List[str]): List of names to be joined.
        separator (str): String used to separate elements.

    Returns:
        str: A single concatenated string.
    """
    return separator.join(names)


if __name__ == "__main__":
    name_list: List[str] = ["Harry", "Rohan", "Shubham"]

    result = join_names(name_list)
    print(result)
