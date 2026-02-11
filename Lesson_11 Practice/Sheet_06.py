class Animal:
    """
    Base class representing a generic animal.

    This class can be extended to define common characteristics
    and behaviors shared by all animals.
    """
    pass


class Pet(Animal):
    """
    Represents domesticated animals that are kept as pets.

    Inherits:
        Animal: Gains the general animal characteristics.
    """
    pass


class Dog(Pet):
    """
    Represents a dog, a specific type of pet.

    Inherits:
        Pet: Gains characteristics of domesticated animals.
    """

    @staticmethod
    def bark() -> None:
        """
        Produce the barking sound associated with dogs.
        """
        print("Bow Bow!")


# Example usage
if __name__ == "__main__":
    dog = Dog()
    dog.bark()
