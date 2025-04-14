# Basic Text Editor CLI

## Description

This project involves creating a simple command-line interface (CLI) text editor. It allows users to perform basic text editing operations on a file, such as opening, reading, writing, and saving content. This project focuses on file I/O, string manipulation, and potentially some basic command parsing.

## Concepts Covered

- File input/output (I/O) operations
- String manipulation
- Command-line argument parsing (optional, but recommended)
- Basic program control flow

## Potential Modules

- `pathlib` (for file path manipulation, checking file existence)
- `argparse` (for accessing command-line arguments)

## Example Usage

```bash
❯ python text_editor.py my_file.txt

"my_file.txt" file opened for editing

❯ read
Wasted Love

❯ append Bara Bada Bastu
Done!

❯ read
*Changes not saved

Wasted Love
Bara Bada Bastu

❯ save
Done!

❯ read
Wasted Love
Bara Bada Bastu

❯ write Wasted Love
Done!

❯ read
*Changes not saved

Wasted Love

❯ save
Done!

❯ read
Wasted Love

❯ exit
Done. Bye!
```

## Steps

- **File Handling:**
  - Accept a filename as a command-line argument.
  - Handle cases where the file exists (open and read) and where it doesn't (create a new file).
- **Command Parsing:**
  - Implement a loop to continuously prompt the user for commands.
  - Parse basic commands like `read`, `write <text>`, `append <text>`, `save`, and `exit`.
- **Read Operation:**
  - The `read` command should display the current content of the file.
- **Write Operation:**
  - The `write <text>` command should overwrite the entire file content with the provided text.
- **Append Operation:**
  - The `append <text>` command should add the provided text to the end of the file.
- **Save Operation:**
  - The `save` command should write the current content (including any edits) back to the file.
- **Exit Operation:**
  - The `exit` command should terminate the editor.
- **Error Handling:**
  - Handle invalid commands or file operations gracefully.

## Future Improvements

- **More Editing Commands:** Implement more sophisticated editing features like inserting text at a specific line, deleting lines, searching, and replacing.
- **Undo/Redo:** Add undo/redo functionality.
- **Line Numbers:** Display line numbers.
- **Syntax Highlighting:** Add syntax highlighting for different file types.
- **GUI:** Create a graphical user interface (GUI).
- **File Locking:** Implement file locking to prevent concurrent modification.
- **Buffering:** Implement efficient buffering for large files.
- **Status Bar:** Display a status bar with file information.
