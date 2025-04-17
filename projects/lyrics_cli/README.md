# Lyrics CLI

## Description

This project involves creating a command-line application that allows users to retrieve lyrics for a specified artist and song title. The application will take the artist name and song title as input and fetch the lyrics from the free [Lyrics.ovh API](https://www.google.com/search?q=https://lyricsovh.docs.apiary.io/%23).

## Concepts Covered

- Making HTTP requests to external APIs
- Handling JSON data (though successful responses are often plain text)
- Command-line argument parsing
- String manipulation and display
- Error handling (network issues, song not found, API errors)

## Potential Modules

- `requests` (for making HTTP requests)
- `json` (for working with JSON data)
- `argparse` (for handling command-line arguments)

## API Information: Lyrics.ovh

- **Base URL:** `https://api.lyrics.ovh/v1/`
- **Endpoint for Lyrics:** `/artist/title` (replace `artist` and `title` with the respective values)
- **Response Format (Success):** JSON with a `lyrics` key containing the lyrics as a string.
- **Response Format (Not Found):** JSON with an `error` key containing a message like `"No lyrics found"`.

## Example Usage

```bash
python lyrics_cli.py --artist "Queen" --title "Bohemian Rhapsody"
python lyrics_cli.py -a "The Beatles" -t "Hey Jude"
```

## Steps

- [x] **Argument Parsing:**

Use `argparse` to handle the following command-line arguments:

- `--artist` or `-a`: The name of the artist (a string, required).
- `--title` or `-t`: The title of the song (a string, required).

- [ ] **Constructing the API Request URL:**

Take the artist and title provided by the user and build the appropriate URL for the Lyrics.ovh API. Remember to handle potential spaces or special characters in the artist and title (URL encoding might be necessary, though this API seems to handle spaces reasonably well).

- [ ] **Fetching Lyrics Data:**

- Use the `requests` library to send an HTTP GET request to the constructed API URL.
- Handle potential network errors (e.g., `requests.exceptions.RequestException`).

- [ ] **Parsing the API Response:**

- If the request is successful (status code 200), the response will likely be in JSON format.
- Use the `json` library to parse the JSON data.
- Check if the response contains the lyrics key. If it does, extract and display the lyrics.
- If the response contains an `error` key (e.g., "No lyrics found"), display an appropriate message to the user.

- [ ] **Displaying the Lyrics:**

Print the retrieved lyrics to the console.

- [ ] **Error Handling:**

Implement error handling for scenarios such as:

- Network issues during the API request.
- API returning an error message (e.g., "No lyrics found").
- Unexpected format of the JSON response.

## Future Improvements

- **Saving Lyrics to a File:** Allow users to save the retrieved lyrics to a text file.
- **Searching for Songs by Artist:** Implement functionality to search for songs by a given artist (if the API supports it).
- **Handling Special Characters:** Ensure proper handling of various special characters in artist and song titles.
- **More Robust Error Messages:** Provide more informative error messages to the user.
