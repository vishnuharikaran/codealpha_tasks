# Email Address Extractor

An automated Python script that parses text files, automatically extracts all email addresses using Regular Expressions, removes duplicate entries while preserving order, and saves the unique email addresses to an output file.

## Description

The Email Address Extractor is a command-line task automation tool developed for the **CodeAlpha** Python Programming Internship. Automating text processing tasks eliminates manual searching and copy-pasting. This application reads a target text document (`input.txt`), scans for valid email pattern matches using regex, removes duplicate email entries while preserving their original order of appearance, displays match statistics in the terminal, and exports the unique email addresses to `extracted_emails.txt`.

---

## Features

- **Automated Text Reading**: Reads text content directly from `input.txt` using Python context managers.
- **Regex Pattern Matching**: Scans and extracts all valid email addresses using Python's built-in `re` module.
- **Duplicate Removal & Order Preservation**: Deduplicates extracted emails while maintaining their original appearance order in the source document.
- **Match Statistics**: Reports both total raw email matches found and total unique email addresses extracted.
- **Automated File Saving**: Saves unique email addresses into `extracted_emails.txt` (one email per line).
- **Robust Error Handling**: Safely handles missing files, empty files, files with no email matches, and file permission errors without crashing.

---

## CodeAlpha Requirements Implemented

- ✅ Demonstrated task automation using Python.
- ✅ Automated email address extraction from an unformatted `.txt` file.
- ✅ Automated exporting of extracted results to an output file (`extracted_emails.txt`).
- ✅ Utilized standard library regular expressions (`re` module).
- ✅ Utilized safe context-managed file handling (`with open(...)`).

---

## Technologies Used

- **Language**: Python 3.x
- **Standard Library Modules**: `re` (Regular Expressions)
- **User Interface**: Command Line Interface (CLI) / Terminal

---

## Python Concepts Demonstrated

- **File Handling & Context Managers**: Safe reading and writing of external files (`with open(...)`).
- **Regular Expressions**: Matching pattern sequences (`re.findall()`).
- **Lists & Order Preservation**: Deduplicating lists while retaining initial appearance sequence.
- **Conditional Logic & Loops**: Using `if-else` branching and `for` loops for data processing.
- **Modular Functions**: Organised into single-responsibility functions (`read_input_file`, `extract_emails`, `remove_duplicates`, `display_extracted_emails`, `save_emails_to_file`, `main`).
- **Exception Handling**: Handling `FileNotFoundError`, `PermissionError`, and generic file exceptions using `try-except` blocks.

---

## Project Structure

```text
Task_Automation/
│
├── email_extractor.py       # Main Python automation script
├── input.txt                # Input text file containing unformatted text and email addresses
├── extracted_emails.txt     # (Auto-generated) Contains extracted unique emails (one per line)
└── README.md                # Project documentation
```

*Note: `extracted_emails.txt` is generated automatically when valid email addresses are found.*

---

## How to Run

### Prerequisites

- Python 3.x installed on your computer.

### Instructions

1. Open your terminal or command prompt.
2. Navigate to the project directory:

   ```bash
   cd Task_Automation
   ```

3. Add or edit your target text containing email addresses in `input.txt`.
4. Run the Python script:

   ```bash
   python email_extractor.py
   ```

5. View the extracted email list and match summary in your terminal.
6. Open `extracted_emails.txt` to view the saved results.

---

## Example

### Input (`input.txt`)

```text
Contact us at support@example.com.
You can also email john@gmail.com.
For support, contact support@example.com again.
```

### Terminal Output

```text
==================================================
      TASK AUTOMATION: EMAIL ADDRESS EXTRACTOR    
==================================================

Reading input.txt...

File Contents:
--------------------------------------------------
Contact us at support@example.com.
You can also email john@gmail.com.
For support, contact support@example.com again.
--------------------------------------------------

Extracted Email Addresses:
--------------------------------------------------
support@example.com
john@gmail.com
--------------------------------------------------
Total email matches found: 3
Total unique emails found: 2

Emails successfully saved to extracted_emails.txt
```

### Output File (`extracted_emails.txt`)

```text
support@example.com
john@gmail.com
```

---

## Error Handling

- **Missing `input.txt`**: Catches `FileNotFoundError` and displays `Error: The file 'input.txt' was not found. Please check the file path.` without crashing.
- **Empty `input.txt`**: Detects empty or whitespace-only files, displays `input.txt is empty. No emails to extract.`, and skips output file creation.
- **No Emails Found**: Displays `No email addresses found. Output file was not created.` and refrains from creating an empty file.
- **File Read/Write Permission Errors**: Catches `PermissionError` and displays clear user warning messages without terminating unexpectedly.

---

## Future Improvements

*(Note: The following are optional potential enhancements for future releases and are not part of the current CodeAlpha project build)*

- **Custom Input File Selection**: Allow users to pass custom input file paths via command-line arguments (`sys.argv` or `argparse`).
- **Multi-Format Support**: Support extraction from PDF, DOCX, and HTML documents.
- **CSV / JSON Export**: Provide option to export extracted emails with domain metadata into CSV or JSON format.
- **Graphical User Interface (GUI)**: Build a drag-and-drop desktop UI using `Tkinter` or `CustomTkinter`.
