def divide_numbers() -> None:
    """
    Prompt the user to enter two integers and perform division while
    handling division-by-zero errors gracefully.
    """
    try:
        numerator = int(input("Enter the first number (a): "))
        denominator = int(input("Enter the second number (b): "))

        result = numerator / denominator
        print(f"Result of a / b: {result}")

    except ZeroDivisionError:
        # Handles division by zero
        print("Division by zero is not allowed. Result is undefined (infinite).")

    except ValueError:
        # Handles invalid numeric input
        print("Invalid input. Please enter valid integers.")


if __name__ == "__main__":
    divide_numbers()
