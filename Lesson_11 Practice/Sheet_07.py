class ComplexNumber:
    """
    Represents a complex number supporting arithmetic operations
    such as addition and multiplication using operator overloading.

    Attributes:
        real (float): Real part of the complex number.
        imag (float): Imaginary part of the complex number.
    """

    def __init__(self, real: float, imag: float) -> None:
        """
        Initialize a ComplexNumber instance.

        Args:
            real (float): Real component.
            imag (float): Imaginary component.
        """
        self.real = real
        self.imag = imag

    def __add__(self, other: "ComplexNumber") -> "ComplexNumber":
        """
        Add two complex numbers.

        Args:
            other (ComplexNumber): Another complex number.

        Returns:
            ComplexNumber: Result of addition.

        Raises:
            TypeError: If operand is not a ComplexNumber instance.
        """
        if not isinstance(other, ComplexNumber):
            raise TypeError("Addition is supported only between ComplexNumber instances.")

        return ComplexNumber(
            self.real + other.real,
            self.imag + other.imag
        )

    def __mul__(self, other: "ComplexNumber") -> "ComplexNumber":
        """
        Multiply two complex numbers using the formula:
        (a + bi)(c + di) = (ac − bd) + (ad + bc)i

        Args:
            other (ComplexNumber): Another complex number.

        Returns:
            ComplexNumber: Result of multiplication.

        Raises:
            TypeError: If operand is not a ComplexNumber instance.
        """
        if not isinstance(other, ComplexNumber):
            raise TypeError("Multiplication is supported only between ComplexNumber instances.")

        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real

        return ComplexNumber(real_part, imag_part)

    def __str__(self) -> str:
        """
        Provide a user-friendly string representation.

        Returns:
            str: Complex number formatted as a + bi.
        """
        sign = "+" if self.imag >= 0 else "-"
        return f"{self.real} {sign} {abs(self.imag)}i"

    def __repr__(self) -> str:
        """
        Provide a developer-friendly representation.

        Returns:
            str: Representation useful for debugging.
        """
        return f"ComplexNumber(real={self.real}, imag={self.imag})"


# Example usage
if __name__ == "__main__":
    c1 = ComplexNumber(1, 2)
    c2 = ComplexNumber(3, 4)

    print(c1 + c2)
    print(c1 * c2)
