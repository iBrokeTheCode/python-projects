import pytest

import sys

from projects.currency_converter.currency_converter import get_supported_currencies, parse_arguments, CurrencyConverter, main


@pytest.mark.parametrize('filename, expected', [
    ('404.json', 'Error getting supported currency info'),
    ('supported_currencies.json', 'United States Dollar (USD)'),
])
def test_get_supported_currencies(filename, expected):
    """Test the get_supported_currencies function."""
    assert expected in get_supported_currencies(filename)


def test_parse_arguments():
    """Test the parse_arguments function."""
    sys.argv = ['currency_converter.py', '-f', 'USD', '-t', 'EUR', '-a', '100']

    args = parse_arguments()

    assert args.from_currency == 'USD'
    assert args.to_currency == 'EUR'
    assert args.amount == 100.0


def test_currency_converter_init():
    """Test the CurrencyConverter class initialization."""
    converter = CurrencyConverter()

    assert isinstance(converter.supported_currencies, dict)

    if len(converter.supported_currencies):
        assert converter.supported_currencies.get(
            'USD') == 'United States Dollar'


@pytest.mark.parametrize('from_currency, to_currency, amount', [
    ('USD', 'EUR', 100),
    ('EUR', 'USD', 1),
])
def test_convert_currency(capsys, from_currency, to_currency, amount):
    """Test the convert_currency method."""
    converter = CurrencyConverter()
    converter.convert_currency(from_currency, to_currency, amount)
    captured = capsys.readouterr()

    assert f'{amount:.2f} {from_currency} is equivalent to' in captured.out
