def check_list_length() -> None:
    """
    Demonstrate the use of the assignment expression (walrus operator :=)
    to compute a value and evaluate a condition in a single statement.
    """

    data = [1, 2, 3, 4, 5]

    # The walrus operator assigns the result of len(data) to `length`
    # while simultaneously evaluating the conditional expression.
    if (length := len(data)) > 3:
        print(f"List is too long ({length} elements, expected <= 3)")


if __name__ == "__main__":
    check_list_length()
