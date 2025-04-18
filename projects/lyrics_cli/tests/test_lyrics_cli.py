import pytest

import sys

from projects.lyrics_cli.lyrics_cli import parse_arguments, LyricsApp


@pytest.mark.parametrize('artist, title', [
    ('Nemo', 'The Code'),
    ('JJ', 'Wasted Love')
])
def test_parse_arguments(artist, title):
    """Tests the parse_arguments function."""
    sys.argv = ['test_lyrics_cli.py', '--artist', artist, '--title', title]
    args = parse_arguments()

    assert args.artist == artist
    assert args.title == title


@pytest.mark.parametrize('artist, title, expected', [
    ('Nemo', 'The Code', '"The Code" by Nemo'),
    ('JJ', 'Wasted Love', 'No lyrics found')
])
def test_get_lyrics(capsys, artist, title, expected):
    """Tests the get_lyrics method by doing the API call."""
    sys.argv = ['test_lyrics_cli.py', '--artist', artist, '--title', title]

    app = LyricsApp()
    app.get_lyrics(artist, title)

    captured = capsys.readouterr()

    assert expected in captured.out


def mock_successful_lyrics_fetch(self, artist, title):
    return {"lyrics": "This is the song's lyrics."}


def mock_lyrics_not_found(self, artist, title):
    return {"error": "No lyrics found"}


def test_get_lyrics_success(capsys, monkeypatch):
    """Tests the get_lyrics method when lyrics are successfully fetched."""
    monkeypatch.setattr(LyricsApp, "_LyricsApp__fetch_lyrics",
                        mock_successful_lyrics_fetch)
    app = LyricsApp()
    app.get_lyrics("Nemo", "The Code")
    captured = capsys.readouterr()
    assert '"The Code" by Nemo' in captured.out
    assert "This is the song's lyrics." in captured.out


def test_get_lyrics_not_found(capsys, monkeypatch):
    """Tests the get_lyrics method when no lyrics are found."""
    monkeypatch.setattr(
        LyricsApp, "_LyricsApp__fetch_lyrics", mock_lyrics_not_found)
    app = LyricsApp()
    app.get_lyrics("JJ", "Wasted Love")
    captured = capsys.readouterr()
    assert "No lyrics found" in captured.out
