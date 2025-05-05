class TerminalColors:
    """Class to store ANSI color codes."""
    RESET = '\033[0m'
    FG_RED = '\033[91m'
    FG_GREEN = '\033[92m'
    FG_YELLOW = '\033[93m'
    FG_BLUE = '\033[94m'
    FG_MAGENTA = '\033[95m'
    FG_CYAN = '\033[96m'
    FG_WHITE = '\033[97m'
    BG_RED = '\033[101m'
    BG_GREEN = '\033[102m'
    BG_YELLOW = '\033[103m'
    BG_BLUE = '\033[104m'
    BG_MAGENTA = '\033[105m'
    BG_CYAN = '\033[106m'
    BG_WHITE = '\033[107m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def colored_print(text: str, color: str = TerminalColors.RESET, bold: bool = False, underline: bool = False) -> None:
    """Prints colored text to the terminal."""
    formatting = color
    if bold:
        formatting += TerminalColors.BOLD
    if underline:
        formatting += TerminalColors.UNDERLINE
    print(f'{formatting}{text}{TerminalColors.RESET}')


if __name__ == '__main__':
    # Example usage:
    colored_print('This is red text.', TerminalColors.FG_RED)
    colored_print('This is green bold text.',
                  TerminalColors.FG_GREEN, bold=True)
    colored_print('This is yellow underlined text.',
                  TerminalColors.FG_YELLOW, underline=True)
    colored_print('This is blue bold underlined text.',
                  TerminalColors.FG_BLUE, bold=True, underline=True)
