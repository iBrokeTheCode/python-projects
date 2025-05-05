# Simple Calculator

## Description

A basic command-line calculator that performs fundamental arithmetic operations: addition, subtraction, multiplication, and division. This project aims to solidify understanding of user input, conditional statements, and basic arithmetic operations in Python.

## Concepts Covered

- Basic arithmetic operations (+, -, \*, /)
- User input (`input()`)
- Conditional statements (`if`, `elif`, `else`)
- Error handling (basic `try-except` blocks for division by zero)
- Basic command-line interaction

## Potential Modules

- `argparse` for command-line argument handling.
- `logging` to displaying informative messages.

## Example Usage

```bash
python calculator.py sum 28 7
python calculator.py subtract 28 7
python calculator.py product 28 7
python calculator.py division 28 7

# Output
[2025 Apr 08 - 09:16:23]
(INFO): Result = 196
```

## Steps

- **Get User Input:** Prompt the user to enter two numbers and the desired arithmetic operation.
- **Validate Input:** Ensure the input is numerical and the operation is one of the allowed symbols (+, -, \*, /).
- **Perform Calculation:** Use conditional statements to determine the operation and perform the corresponding calculation.
- **Handle Division by Zero:** Implement error handling to prevent division by zero.
- **Display Result:** Print the calculated result to the console.
