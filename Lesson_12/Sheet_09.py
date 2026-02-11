# Global variable
value: int = 89


def demonstrate_local_scope() -> None:
    """
    Demonstrate how local variables inside a function do not modify
    the global variable unless the `global` keyword is explicitly used.
    """
    # Local variable (does not affect the global variable)
    value = 3
    print(f"Local value inside function: {value}")


if __name__ == "__main__":
    demonstrate_local_scope()

    # The global variable remains unchanged
    print(f"Global value outside function: {value}")
