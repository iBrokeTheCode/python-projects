# Number Guessing Game

## Description

A simple command-line number guessing game where the computer generates a random number, and the player tries to guess it. The game provides feedback to the player, indicating whether their guess is too high or too low, until they guess the correct number.

## Concepts Covered

- User input and output
- Conditional statements and loops
- Random number generation (`random` module)
- Basic game logic

## Potential Modules

- `random` (for generating random numbers)

## Example Usage

```bash
python number_guessing_game.py
# Example output:
# Guess a number between 1 and 100: 50
# > Too high!

# Guess a number between 1 and 100: 25
# > Too low!

# Guess a number between 1 and 100: 39

# > Congratulations! You guessed the number in 7 tries

# Play again? (y/n): y
# ...
```

## Steps

- **Generate a Random Number:** Use the random module to generate a random number within a specified range.
- **Get User Input:** Prompt the user to enter their guess.
- **Check Guess:** Compare the user's guess to the generated number.
- **Provide Feedback:** Display whether the guess is too high, too low, or correct.
- **Track Attempts:** Keep track of the number of attempts the user has made.
- **End Game:** End the game when the user guesses the correct number.
- **Display Results:** Display the number of attempts it took the user to guess the number.
- **Handle Invalid Input:** Implement error handling for invalid user input.
- **Play Again:** Prompt the user to play again.

## Future Improvements

- **Difficulty Levels:** Implement difficulty levels to change the range of the random number.
- **Limited Attempts:** Limit the number of attempts the user can make.
- **GUI:** Create a graphical user interface (GUI) using Tkinter, PyQt, Flet etc.
- **Multiplayer Mode:** Implement a multiplayer mode where multiple users can guess the number.
