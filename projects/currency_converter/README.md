# Currency Converter CLI

## Description

This project involves creating a command-line application that allows users to convert amounts between different currencies. The application will take the source currency, the target currency, and the amount to convert as input. It will then fetch the latest exchange rates and display the converted amount.

## Concepts Covered

- Making HTTP requests to external APIs
- Handling JSON data
- Command-line argument parsing
- Basic arithmetic operations
- Error handling (network issues, invalid currency codes, etc.)

## Potential Modules

- `requests` (for making HTTP requests)
- `json` (for working with JSON data)
- `argparse` (for handling command-line arguments)

## Potential APIs for Exchange Rates

You'll need to find a reliable API that provides up-to-date currency exchange rates. Some popular options include:

- **Free APIs (may have limitations):**
  - [FreeCurrencyAPI](https://freecurrencyapi.com/)
  - [Exchangerate-API](https://exchangerate-api.com/)
  - [Open Exchange Rates](https://openexchangerates.org/) (requires an API key)
- **Consider the terms of service and any limitations (e.g., request limits, supported currencies) of the API you choose.**

## Example Usage

```bash
python currency_converter.py --from USD --to EUR --amount 100
python currency_converter.py -f GBP -t JPY -a 50.75
```

## Steps

**Choose an Exchange Rate API:**

Selected Free API (Open API version): <a href="https://www.exchangerate-api.com">Rates By Exchange Rate API</a>

- Sign up for an API key if required.
- Familiarize yourself with the [API documentation](https://www.exchangerate-api.com/docs/python-currency-api), especially the endpoints for fetching exchange rates.
- Understand how to specify the base currency and the target currency.

**Argument Parsing:**

Use argparse to handle the following command-line arguments:

- `--from` or `-f`: The source currency code (e.g., USD, EUR, GBP).
- `--to` or `-t`: The target currency code (e.g., EUR, JPY, CAD).
- `--amount` or `-a`: The amount to convert (a floating-point number).

**Fetching Exchange Rates:**

- Construct the appropriate URL to make a request to the chosen API based on the source and target currencies.
- Use the `requests` library to send an HTTP GET request to the API endpoint.
- Handle potential network errors (e.g., `requests.exceptions.RequestException`).

**Parsing JSON Response:**

- If the API request is successful, the response will likely be in JSON format.
- Use the `json` library to parse the JSON data.
- Examine the structure of the JSON response to find the exchange rate for the specified currency pair.

**Performing the Conversion:**

- Extract the exchange rate from the parsed JSON data.
- Multiply the input amount by the exchange rate to get the converted amount.

**Displaying the Result:**

Print the converted amount in a user-friendly format, including the original amount, source currency, target currency, and the converted amount.

**Error Handling:**

Implement error handling for various scenarios, such as:

- Invalid currency codes provided by the user (the API might return an error).
- Errors during the API request (network issues).
- Unexpected format of the JSON response.
- Invalid input amount (e.g., non-numeric).

## Future Improvements

- **Support for More APIs:** Allow users to choose from different exchange rate APIs.
- **Caching of Exchange Rates:** Implement caching to reduce the number of API calls for frequently used currency pairs.
- **More Detailed Output:** Include the date and time of the exchange rate.
- **Interactive Mode:** Allow users to enter conversions without specifying all arguments on the command line.
- **Configuration Options:** Allow users to configure default currencies or API keys.
