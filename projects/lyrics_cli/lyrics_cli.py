import argparse
import requests
import json
from pathlib import Path

# ================================================================
#                             COLORS
# ================================================================


class Colors:
    """Class to define color codes for terminal output."""
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    CYAN = '\033[36m'
    RESET = '\033[0m'

    @staticmethod
    def style_text(text: str, color: str) -> str:
        """Apply color to the text."""
        return f'{color}{text}{Colors.RESET}'

# ================================================================
#                              PARSER
# ================================================================


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description='Lyrics App',
        usage='python lyrics_cli.py --artist "Nemo" --title "The Code"',
        epilog='Credits to lyrics.ovh. Visit https://lyricsovh.docs.apiary.io/#reference/0/lyrics-of-a-song/search'
    )

    parser.add_argument(
        '--artist', '-a',
        type=str,
        help='the name of the artist or band',
        required=True,
        dest='artist',
        metavar='artist',
    )

    parser.add_argument(
        '--title', '-t',
        type=str,
        help='the title of the song',
        required=True,
        dest='title',
        metavar='title'
    )

    return parser.parse_args()


# ================================================================
#                              MAIN
# ================================================================


def main() -> None:
    args = parse_arguments()
    print(args)


if __name__ == '__main__':
    main()
