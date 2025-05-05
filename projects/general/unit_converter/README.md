# Unit Converter

## Description

A command-line tool to convert between various units of measurement. This project will allow users to convert between different units for length, temperature, weight, and potentially other categories.

## Concepts Covered

- User input and output
- Conditional statements (`if`, `elif`, `else`)
- Dictionaries (to store conversion factors)
- Basic arithmetic operations
- Error handling (for invalid input or units)
- Command-line interface (CLI)

## Potential Modules

- `argparse` (for parsing command-line arguments)
- `sys` (for system-specific parameters and functions)

## Example Usage

```bash
py unit_converter.py --category length --from meters --to centimeters --value 1
1.0 meters is equal to 100.0 centimeters

py unit_converter.py --category weight --from kilograms --to grams --value 1
1.0 kilograms is equal to 1000.0 grams

py unit_converter.py --category temperature --from celsius --to fahrenheit --value 1
1.0 celsius is equal to 33.8 fahrenheit

py unit_converter.py --category temperature --from celsius --to meters --value 1
Value Error: --to unit no supported
```

## Steps

- **Define Units and Conversion Factors:** Create dictionaries to store the units and their corresponding conversion factors.
- **Get User Input:** Prompt the user to enter the value, the original unit, and the target unit. Or use command line arguments.
- **Validate Input:** Ensure the entered units are valid and the value is a number.
- **Perform Conversion:** Retrieve the conversion factors from the dictionaries and perform the calculation.
- **Display Result:** Print the converted value along with the original and target units.
- **Implement Error Handling:** Handle cases where the user enters invalid units or non-numeric values.
