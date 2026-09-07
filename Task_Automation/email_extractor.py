"""
CodeAlpha - Task Automation: Email Address Extractor
An automated script to extract email addresses from text files using Python 3.
"""


def read_input_file(filename="input.txt"):
    """Read and return the text content of the specified file with error handling."""
    print(f"Reading {filename}...\n")
    try:
        with open(filename, mode="r", encoding="utf-8") as file:
            file_content = file.read()
            return file_content
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found. Please check the file path.")
        return None
    except Exception as error:
        print(f"Error reading file '{filename}': {error}")
        return None


def main():
    """Main entry point for the Email Address Extractor application."""
    print("=" * 50)
    print("      TASK AUTOMATION: EMAIL ADDRESS EXTRACTOR    ")
    print("=" * 50)
    print()

    # Read input file contents (Phase 2)
    file_content = read_input_file("input.txt")

    if file_content is not None:
        print("File Contents:")
        print("-" * 50)
        print(file_content.strip())
        print("-" * 50)
        print("\nEmail extraction will be implemented in the next phase.\n")


if __name__ == "__main__":
    main()

