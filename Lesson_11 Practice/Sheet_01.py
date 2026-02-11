from typing import Iterable, List


class Vector:
    """
    Represents a mathematical vector that stores a collection of numeric values
    and supports built-in Python operations such as length retrieval.

    Attributes:
        values (List[float]): A list containing the elements of the vector.
    """

    def __init__(self, values: Iterable[float]) -> None:
        """
        Initialize the Vector instance.

        Args:
            values (Iterable[float]): A sequence or iterable containing
                                     numeric vector elements.
        """
        self.values: List[float] = list(values)

    def __len__(self) -> int:
        """
        Return the number of elements in the vector.

        Returns:
            int: The length (dimension) of the vector.
        """
        return len(self.values)

    def __repr__(self) -> str:
        """
        Provide a developer-friendly string representation of the vector.

        Returns:
            str: Representation of the vector object.
        """
        return f"Vector(values={self.values})"


# Example usage
if __name__ == "__main__":
    vector = Vector([1, 2, 3])
    print(len(vector))
