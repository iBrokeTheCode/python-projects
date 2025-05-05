import argparse
from secrets import choice
from random import shuffle
from string import ascii_uppercase, ascii_lowercase, digits, punctuation


# ================================================================
#                             PARSER
# ================================================================


def parse_arguments() -> argparse.Namespace:
    """Parses command-line arguments for the password generator."""

    parser = argparse.ArgumentParser(description='Password Generator')

    parser.add_argument(
        '-l', '--length',
        type=int,
        help='the length of the password (default is 8)',
        metavar='length'
    )

    parser.add_argument(
        '-u', '--uppercase',
        help='include uppercase letters',
        action='store_true'
    )

    parser.add_argument(
        '-w', '--lowercase',
        help='include lowercase letters',
        action='store_true'
    )

    parser.add_argument(
        '-d', '--digits',
        help='include digits',
        action='store_true'
    )

    parser.add_argument(
        '-s', '--symbols',
        help='include symbols',
        action='store_true'
    )

    return parser.parse_args()

# ================================================================
#                           PASSWORD GENERATOR
# ================================================================


def generate_password(length: int, has_upper: bool, has_lower: bool, has_digits: bool, has_symbols: bool) -> str:
    """Generates a password with specified criteria."""

    # Validate length at least 8
    if length < 8:
        print(
            '\033[33mPassword must be at least 8 length. Set to 8 characters\033[0m')
        length = 8

    # Variables
    characters_set = []
    password = []

    # Add at least one character of each type
    password.append(choice(ascii_uppercase))
    password.append(choice(ascii_lowercase))
    password.append(choice(digits))
    password.append(choice(punctuation))

    # Removing characters set if their False
    if has_upper:
        characters_set.append(ascii_uppercase)
    if has_lower:
        characters_set.append(ascii_lowercase)
    if has_digits:
        characters_set.append(digits)
    if has_symbols:
        characters_set.append(punctuation)

    # Convert list to string (validate if the characters_set is empty)
    if not characters_set:
        characters_set = [
            ascii_uppercase, ascii_lowercase, digits, punctuation]
    characters_set = ''.join(characters_set)

    # Generate the rest of the password
    remaining_length = length - len(password)

    for _ in range(remaining_length):
        password.append(choice(characters_set))

    # Shuffle password
    shuffle(password)

    return ''.join(password)

# ================================================================
#                               MAIN
# ================================================================


def main() -> None:
    """Main function to execute the password generator."""

    args = parse_arguments()

    length = args.length or 8
    upper = args.uppercase
    lower = args.lowercase
    digits = args.digits
    symbols = args.symbols

    password = generate_password(length, upper, lower, digits, symbols)
    print(f'Your password: \033[32m{password}\033[0m')


if __name__ == '__main__':
    main()
