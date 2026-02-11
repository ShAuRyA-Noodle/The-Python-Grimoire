class TwoDVector:
    """
    Represents a two-dimensional vector.

    Attributes:
        x (float): The x-component of the vector.
        y (float): The y-component of the vector.
    """

    def __init__(self, x: float, y: float) -> None:
        """
        Initialize a 2D vector.

        Args:
            x (float): The x-component.
            y (float): The y-component.
        """
        self.x = x
        self.y = y

    def show(self) -> None:
        """
        Display the vector in standard mathematical form.
        """
        print(f"The vector is {self.x}i + {self.y}j")

    def __repr__(self) -> str:
        """
        Return a developer-friendly string representation.

        Returns:
            str: Representation of the 2D vector.
        """
        return f"TwoDVector(x={self.x}, y={self.y})"


class ThreeDVector(TwoDVector):
    """
    Represents a three-dimensional vector extending the TwoDVector class.

    Inherits:
        TwoDVector: Provides x and y components.

    Attributes:
        z (float): The z-component of the vector.
    """

    def __init__(self, x: float, y: float, z: float) -> None:
        """
        Initialize a 3D vector.

        Args:
            x (float): The x-component.
            y (float): The y-component.
            z (float): The z-component.
        """
        super().__init__(x, y)
        self.z = z

    def show(self) -> None:
        """
        Display the vector in 3D mathematical form.
        """
        print(f"The vector is {self.x}i + {self.y}j + {self.z}k")

    def __repr__(self) -> str:
        """
        Return a developer-friendly string representation.

        Returns:
            str: Representation of the 3D vector.
        """
        return f"ThreeDVector(x={self.x}, y={self.y}, z={self.z})"


# Example usage
if __name__ == "__main__":
    vector_2d = TwoDVector(1, 2)
    vector_2d.show()

    vector_3d = ThreeDVector(5, 2, 3)
    vector_3d.show()
