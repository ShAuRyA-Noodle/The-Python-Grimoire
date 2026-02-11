from typing import Union


class Vector:
    """
    Represents a three-dimensional mathematical vector supporting
    vector addition and dot-product multiplication.

    Attributes:
        x (float): X-component of the vector.
        y (float): Y-component of the vector.
        z (float): Z-component of the vector.
    """

    def __init__(self, x: float, y: float, z: float) -> None:
        """
        Initialize a 3D vector.

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
            Vector: A new Vector containing the result of addition.

        Raises:
            TypeError: If the operand is not a Vector.
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
        Perform dot product multiplication using the * operator.

        Args:
            other (Vector): Another vector.

        Returns:
            float: Dot product of the two vectors.

        Raises:
            TypeError: If the operand is not a Vector.
        """
        if not isinstance(other, Vector):
            raise TypeError("Multiplication is supported only between Vector instances.")

        return (
            self.x * other.x +
            self.y * other.y +
            self.z * other.z
        )

    def __repr__(self) -> str:
        """
        Provide an official developer-friendly representation.

        Returns:
            str: Representation of the Vector object.
        """
        return f"Vector(x={self.x}, y={self.y}, z={self.z})"

    def __str__(self) -> str:
        """
        Provide a user-friendly string representation.

        Returns:
            str: Human-readable vector representation.
        """
        return f"Vector({self.x}, {self.y}, {self.z})"


# Example usage
if __name__ == "__main__":
    v1 = Vector(1, 2, 3)
    v2 = Vector(4, 5, 6)
    v3 = Vector(7, 8, 9)

    print(v1 + v2)  # Vector(5, 7, 9)
    print(v1 * v2)  # 32

    print(v1 + v3)  # Vector(8, 10, 12)
    print(v1 * v3)  # 50
