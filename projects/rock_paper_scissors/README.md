# Rock, Paper, Scissors Game

## Description

A command-line implementation of the classic Rock, Paper, Scissors game. This project allows users to play against the computer, with the computer's choice being randomly generated. The game tracks the user's and computer's scores, and displays the results of each round.

## Concepts Covered

- User input and output
- Conditional statements and loops
- Randomization (`random` module)
- Basic game logic

## Potential Modules

- `random` (for generating the computer's choice)

## Example Usage

```bash
python rock_paper_scissors.py
# Example output:
# Enter your choice (rock, paper, scissors): paper
# Computer chose: paper
# It is a tie!
# Score [user/computer]: 0/0 victories

# Do you want to play again? (yes/no): yes
# ...
```

## Steps

- **Get User Input:** Prompt the user to enter their choice (rock, paper, or scissors).
- **Generate Computer Choice:** Use the random module to generate the computer's choice.
- **Determine Winner:** Implement the game logic to determine the winner of each round.
- **Update Scores:** Keep track of the user's and computer's scores.
- **Display Results:** Display the results of each round, including the user's and computer's choices and the winner.
- **Play Again:** Prompt the user to play again.
- **Handle Invalid Input:** Implement error handling for invalid user input.

## Future Improvements

- **GUI:** Create a graphical user interface (GUI) using Tkinter, PyQt, Flet etc.
- **Best-of-N Games:** Allow users to play a best-of-N series.
- **Score History:** Store and display the user's score history.
- **Multiplayer Mode:** Implement a multiplayer mode where two users can play against each other.
