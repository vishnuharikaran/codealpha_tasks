import re

# Simple and readable regex pattern to match email addresses
# Matches: username @ domain . top-level-domain
EMAIL_REGEX = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"


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


def extract_emails(text_content):
    """Extract all email addresses from text content using regular expressions."""
    if not text_content:
        return []
    extracted_emails = re.findall(EMAIL_REGEX, text_content)
    return extracted_emails


def display_extracted_emails(extracted_emails):
    """Display the list of extracted email addresses and total count."""
    print("\nExtracted Email Addresses:")
    print("-" * 50)

    if not extracted_emails:
        print("No email addresses found.")
    else:
        for email in extracted_emails:
            print(email)

    print("-" * 50)
    print(f"Total emails found: {len(extracted_emails)}")


def main():
    """Main entry point for the Email Address Extractor application."""
    print("=" * 50)
    print("      TASK AUTOMATION: EMAIL ADDRESS EXTRACTOR    ")
    print("=" * 50)
    print()

    # Step 1: Read input file contents
    file_content = read_input_file("input.txt")

    if file_content is not None:
        print("File Contents:")
        print("-" * 50)
        print(file_content.strip())
        print("-" * 50)

        # Step 2: Extract email addresses (Phase 3)
        emails = extract_emails(file_content)

        # Step 3: Display results
        display_extracted_emails(emails)


if __name__ == "__main__":
    main()


