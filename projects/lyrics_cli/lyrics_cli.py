import argparse
import requests
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
    """Parses command-line arguments for the Lyrics App."""
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
#                          LYRICS API
# ================================================================


class LyricsApp:
    """A class to fetch and display lyrics from the Lyrics.ovh API."""

    LYRICS_URL = 'https://api.lyrics.ovh/v1/{artist}/{title}'

    def __fetch_lyrics(self, artist: str, title: str) -> dict | None:
        """
        Fetches lyrics from the Lyrics.ovh API.

        Args:
            artist (str): The name of the artist.
            title (str): The title of the song.

        Returns:
            dict or None: A dictionary containing the API response in JSON format,
                         or None if an error occurred.
        """
        try:
            response = requests.get(
                self.LYRICS_URL.format(artist=artist, title=title))
            if response.status_code == 200 or response.status_code == 404:
                return response.json()
            else:
                response.raise_for_status()
                print(Colors.style_text(
                    f'Error: Unexpected status code {response.status_code} from API.', Colors.RED))
                return None
        except requests.RequestException as e:
            print(Colors.style_text(
                f'Error fetching lyrics: {e}', Colors.RED))
            return None

    def __display_lyrics(self, artist: str, title: str, lyrics: str) -> None:
        """
        Displays the lyrics to the console with artist and title.

        Args:
            artist (str): The name of the artist.
            title (str): The title of the song.
            lyrics (str): The lyrics of the song.
        """
        print(Colors.style_text(
            f'"{title.title()}" by {artist.title()}\n', Colors.GREEN))
        print(
            Colors.style_text(lyrics, Colors.YELLOW))

    def get_lyrics(self, artist: str, title: str) -> None:
        """
        Fetches lyrics and displays them to the user.

        Args:
            artist (str): The name of the artist.
            title (str): The title of the song.
        """
        print(Colors.style_text('Lyrics App\n', Colors.CYAN))

        response = self.__fetch_lyrics(artist, title)

        if response and 'lyrics' in response:
            lyrics = response['lyrics']
            self.__display_lyrics(artist, title, lyrics)
        elif response and 'error' in response:
            print(Colors.style_text(response.get(
                'error', 'No lyrics found'), Colors.RED))


# ================================================================
#                              MAIN
# ================================================================


def main() -> None:
    """Main function to run the Lyrics App."""
    args = parse_arguments()
    artist = args.artist
    title = args.title

    lyrics_app = LyricsApp()
    lyrics_app.get_lyrics(artist, title)


if __name__ == '__main__':
    main()
