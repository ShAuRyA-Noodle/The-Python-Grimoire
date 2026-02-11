def perform_division() -> None:
    """
    Prompt the user for two numbers and perform division while
    explicitly validating that division by zero does not occur.

    Raises:
        ZeroDivisionError: If the second number entered is zero.
    """
    try:
        numerator = int(input("Enter the first number: "))
        denominator = int(input("Enter the second number: "))

        if denominator == 0:
            raise ZeroDivisionError(
                "Division by zero is not allowed in this program."
            )

        result = numerator / denominator
        print(f"The result of the division is: {result}")

    except ValueError:
        print("Invalid input. Please enter valid integers.")

    except ZeroDivisionError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    perform_division()
