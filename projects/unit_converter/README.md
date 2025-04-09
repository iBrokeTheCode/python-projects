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
python unit_converter.py --from meters --to feet --value 10
10 meters is equal to 32.8084 feet.

python unit_converter.py --from celsius --to fahrenheit --value 25
25 celsius is equal to 77.0 fahrenheit.
```

## Steps

- **Define Units and Conversion Factors:** Create dictionaries to store the units and their corresponding conversion factors.
- **Get User Input:** Prompt the user to enter the value, the original unit, and the target unit. Or use command line arguments.
- **Validate Input:** Ensure the entered units are valid and the value is a number.
- **Perform Conversion:** Retrieve the conversion factors from the dictionaries and perform the calculation.
- **Display Result:** Print the converted value along with the original and target units.
- **Implement Error Handling:** Handle cases where the user enters invalid units or non-numeric values.
