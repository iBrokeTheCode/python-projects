# Password Generator

## Description

A command-line tool to generate strong, random passwords with customizable length and character sets. This project will allow users to specify the desired password length and choose which character types to include (uppercase letters, lowercase letters, digits, symbols).

## Concepts Covered

- Cryptographically secure random number generation (`secrets` module)
- Shuffle items (`random` module)
- String manipulation
- User input and command-line arguments (`argparse`)
- Lists and string methods
- Error handling

## Potential Modules

- `random`
- `secrets`
- `argparse`
- `string` (for character sets)

## Example Usage

```bash
python password_generator.py --length 12 --uppercase --lowercase --digits --symbols
# Your password: aB9$xYz!2pQ8

python password_generator.py -l 16 -u -d
# Your password: 7G2pX9aL3kF1vC5z

python password_generator.py
# Your password: on%lf5O$
```

## Steps

- **Get User Input:** Use argparse to get the desired password length and character set options from the command line.
- **Define Character Sets:** Create strings or lists containing the characters for uppercase letters, lowercase letters, digits, and symbols.
- **Generate Random Password:**
  - Create an empty string or list to store the password.
  - Use a loop to generate random characters based on the user's selected character sets.
  - Append the generated characters to the password string or list.
- **Display Password:** Print the generated password to the console.
- **Implement Error Handling:** Handle cases where the user provides invalid input (e.g., negative length).

## Future Improvements

- **GUI:** Create a graphical user interface (GUI) using Tkinter, PyQt, Flet etc.
- **Password Saving:** Implement functionality to save generated passwords to a file or password manager.
- **Password Strength Check:** Integrate a password strength checking library or algorithm to provide feedback on the generated password's strength.
- **Clipboard Integration:** Add an option to copy the generated password to the clipboard.
- **Password History:** Store and display recently generated passwords.
