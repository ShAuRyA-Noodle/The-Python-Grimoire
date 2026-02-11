class Vector:
    """
    Represents a three-dimensional mathematical vector supporting
    vector addition and dot-product multiplication through operator
    overloading.

    Attributes:
        x (float): X-component of the vector.
        y (float): Y-component of the vector.
        z (float): Z-component of the vector.
    """

    def __init__(self, x: float, y: float, z: float) -> None:
        """
        Initialize a Vector instance.

        Args:
            x (float): X-component.
            y (float): Y-component.
            z (float): Z-component.
        """
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other: "Vector") -> "Vector":
        """
        Perform vector addition using the + operator.

        Args:
            other (Vector): Another vector to add.

        Returns:
            Vector: A new vector representing the result of addition.

        Raises:
            TypeError: If the operand is not a Vector instance.
        """
        if not isinstance(other, Vector):
            raise TypeError("Addition is supported only between Vector instances.")

        return Vector(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z,
        )

    def __mul__(self, other: "Vector") -> float:
        """
        Compute the dot product using the * operator.

        Args:
            other (Vector): Another vector.

        Returns:
            float: Dot product of the two vectors.

        Raises:
            TypeError: If the operand is not a Vector instance.
        """
        if not isinstance(other, Vector):
            raise TypeError("Multiplication is supported only between Vector instances.")

        return (
            self.x * other.x +
            self.y * other.y +
            self.z * other.z
        )

    def __str__(self) -> str:
        """
        Provide a human-readable representation of the vector.

        Returns:
            str: Vector displayed in i, j, k component form.
        """
        return f"{self.x}i + {self.y}j + {self.z}k"

    def __repr__(self) -> str:
        """
        Provide an official developer-friendly representation.

        Returns:
            str: Representation useful for debugging.
        """
        return f"Vector(x={self.x}, y={self.y}, z={self.z})"


# Example usage
if __name__ == "__main__":
    v1 = Vector(1, 2, 3)
    v2 = Vector(4, 5, 6)
    v3 = Vector(7, 8, 9)

    print(v1 + v2)
    print(v1 * v2)

    print(v1 + v3)
    print(v1 * v3)
