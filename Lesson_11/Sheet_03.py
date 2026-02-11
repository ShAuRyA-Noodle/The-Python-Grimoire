class Number:
    """
    Represents a numeric wrapper that supports arithmetic operations
    through operator overloading.

    Attributes:
        value (float): The numeric value stored in the Number instance.
    """

    def __init__(self, value: float) -> None:
        """
        Initialize the Number instance.

        Args:
            value (float): The numeric value to store.
        """
        self.value = value

    def __add__(self, other: "Number") -> "Number":
        """
        Overload the addition operator (+) to allow addition between
        two Number objects.

        Args:
            other (Number): Another Number instance to be added.

        Returns:
            Number: A new Number instance containing the result
                    of the addition.

        Raises:
            TypeError: If the operand is not an instance of Number.
        """
        if not isinstance(other, Number):
            raise TypeError("Addition is supported only between Number instances.")

        return Number(self.value + other.value)

    def __repr__(self) -> str:
        """
        Provide an official string representation of the object,
        useful for debugging and logging.

        Returns:
            str: String representation of the Number object.
        """
        return f"Number(value={self.value})"


# Example usage
if __name__ == "__main__":
    num1 = Number(1)
    num2 = Number(2)

    result = num1 + num2
    print(result)  # Output: Number(value=3)
