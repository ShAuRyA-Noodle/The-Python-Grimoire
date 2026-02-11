from typing import List


def read_files(file_paths: List[str]) -> None:
    """
    Attempt to read multiple files and display their contents.
    If a file cannot be opened, the corresponding error is handled
    gracefully without stopping the program.

    Args:
        file_paths (List[str]): A list of file names or paths to read.
    """
    for file_path in file_paths:
        try:
            with open(file_path, "r") as file:
                print(f"\nContents of {file_path}:\n{file.read()}")
        except FileNotFoundError:
            print(f"Error: The file '{file_path}' was not found.")
        except Exception as error:
            print(f"An unexpected error occurred while reading '{file_path}': {error}")


if __name__ == "__main__":
    files_to_read = ["1.txt", "2.txt", "3.txt"]
    read_files(files_to_read)

    print("\nThank you!")
