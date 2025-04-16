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
#                             PARSER
# ================================================================


def get_supported_currencies(data_filename: str) -> str:
    """Fetches the list of supported currencies from a local JSON file."""
    json_path = Path(__file__).parent / data_filename

    try:
        with open(json_path) as file:
            content: dict = json.load(file)

        formatted_content = []
        for key, value in content.items():
            formatted_content.append(f'{value} ({key})')
        return ' | '.join(formatted_content)
    except:
        return f'Error getting supported currency info. Visit https://api.frankfurter.dev/v1/currencies'


def validate_positive_amount(amount: str) -> float:
    """Validates that the amount is positive."""
    if not amount.isdigit():
        raise argparse.ArgumentTypeError(f'"{amount}" is not a valid number')

    number = float(amount)

    if number <= 0:
        raise argparse.ArgumentTypeError(
            f'"{amount}" must be greater than zero')
    return number


def parse_arguments() -> argparse.Namespace:
    """Parse command-line arguments."""
    supported_currencies = get_supported_currencies(
        'supported_currencies.json')
    parser = argparse.ArgumentParser(
        description=f'Supported Currencies: {supported_currencies}',
        epilog='Credits to https://frankfurter.dev',
        usage='python currency_converter.py -f USD -t EUR 100')

    parser.add_argument(
        '--from', '-f',
        dest='from_currency',
        type=str,
        required=True,
        help='currency to convert from')

    parser.add_argument(
        '--to', '-t',
        dest='to_currency',
        type=str,
        required=True,
        help='currency to convert to'
    )

    parser.add_argument(
        '--amount', '-a',
        type=validate_positive_amount,
        required=True,
        help='amount to convert'
    )

    return parser.parse_args()

# ================================================================
#                        CURRENCY CONVERTER
# ================================================================


class CurrencyConverter:
    """A class to handle currency conversion using the Frankfurter API."""

    CONVERSION_URL = 'https://api.frankfurter.dev/v1/latest?base={from_currency}&symbols={to_currency}'
    SUPPORTED_CURRENCIES_URL = 'https://api.frankfurter.dev/v1/currencies'

    def __init__(self) -> None:
        """Initializes the CurrencyConverter."""
        self.supported_currencies = self.__fetch_supported_currencies()

    def __fetch_supported_currencies(self) -> dict:
        """Fetches the list of supported currencies from the API."""
        try:
            response = requests.get(self.SUPPORTED_CURRENCIES_URL)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(Colors.style_text(
                'Error fetching supported currencies: {e}', Colors.RED))
            return {}

    def __is_currency_supported(self, currency: str) -> bool:
        """Checks if a given currency code is supported by the API."""
        return currency.upper() in self.supported_currencies

    def __fetch_exchange_rate(self, from_currency: str, to_currency: str) -> dict | None:
        """Fetches the exchange rate data from the API."""
        if not self.__is_currency_supported(from_currency):
            print(Colors.style_text(
                f'Error: {from_currency} is not a supported currency', Colors.RED))
            return None
        if not self.__is_currency_supported(to_currency):
            print(Colors.style_text(
                f'Error: {to_currency} is not a supported currency', Colors.RED))
            return None

        try:
            response = requests.get(
                CurrencyConverter.CONVERSION_URL.format(
                    from_currency=from_currency, to_currency=to_currency)
            )
            response.raise_for_status()

            return response.json()
        except requests.RequestException as e:
            print(Colors.style_text(
                f'Error during conversion request: {e}', Colors.RED))
            return None
        except ValueError:
            print(Colors.style_text(
                'Error: Could not decode JSON response from the API', Colors.RED))
            return None

    def __get_conversion(self, exchange_data: dict | None, amount: float) -> float | None:
        """Calculates the converted amount based on the exchange rate data."""
        if not exchange_data:
            return

        # exchange_data: {'amount': 1.0, 'base': 'USD', 'date': '2025-04-15', 'rates': {'EUR': 0.88308}}
        if 'rates' in exchange_data:
            rates = exchange_data.get('rates')  # {'EUR': 0.88308}

            if not rates:
                print(Colors.style_text(
                    'Error: Rates data is missing in the API response', Colors.RED))
                return None

            exchange_rate = list(rates.values())[0]
            return amount * exchange_rate
        elif 'message' in exchange_data:
            print(Colors.style_text(
                f'API Error: {exchange_data.get('message', 'Not Found')}', Colors.RED))
            return None
        else:
            print(Colors.style_text(
                'Error: Could not retrieve exchange rate', Colors.RED))
            return None

    def convert_currency(self, from_currency: str, to_currency: str, amount: float) -> None:
        """Converts the given amount from one currency to another."""
        exchange_data = self.__fetch_exchange_rate(from_currency, to_currency)
        converted_amount = self.__get_conversion(exchange_data, amount)

        if converted_amount:
            print(Colors.style_text(
                f'{amount:.2f} {from_currency} is equivalent to {converted_amount:.2f} {to_currency}', Colors.GREEN))

# ================================================================
#                              MAIN
# ================================================================


def main() -> None:
    """Main function to handle command-line arguments and perform currency conversion."""
    args = parse_arguments()
    from_currency = args.from_currency
    to_currency = args.to_currency
    amount = args.amount

    converter = CurrencyConverter()
    converter.convert_currency(from_currency, to_currency, amount)


if __name__ == '__main__':
    main()
