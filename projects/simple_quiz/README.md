# Simple Quiz

## Description

A command-line quiz application that presents users with multiple-choice questions. This project will allow users to take a quiz, track their score, and provide feedback on their answers.

## Concepts Covered

- Dictionaries and lists
- File handling (JSON)
- User input and output
- Conditional statements and loops
- Randomization (`random` module)

## Modules Used

- `json` (for reading quiz questions from a file)
- `random` (for shuffling questions and answer options)

## Example Usage

```bash
python simple_quiz.py quiz_data.json
# Example output:
# Question 1: What is the capital of France?
# a) London
# b) Paris
# c) Berlin
# d) Rome
# Your answer: b
# Correct!
# ...
# Your score: 3/5
```

## Steps

- **Define Quiz Data:** Create a JSON file to store the quiz questions and answers.
- **Read Quiz Data:** Use the json module to read the quiz data from the JSON file.
- **Present Questions:**
  - Loop through the questions and display them to the user.
  - Shuffle the answer options to randomize their order.
- **Get User Input:** Prompt the user to enter their answer.
- **Check Answer:** Compare the user's answer to the correct answer.
- **Provide Feedback:** Display whether the answer was correct or incorrect.
- **Track Score:** Keep track of the user's score.
- **Display Score:** Display the final score to the user.
- **Implement Error Handling:** Handle cases where the user enters invalid input or the JSON file is not found.

## Future Improvements

- **Different Question Types:** Add support for different question types (e.g., true/false, fill-in-the-blank).
- **Difficulty Levels:** Implement difficulty levels to categorize questions.
- **Timers:** Add timers to limit the time for each question.
- **GUI:** Create a graphical user interface (GUI) using Tkinter, PyQt, Flet etc.
- **User Profiles:** Implement user profiles to store scores and track progress.
- **Question Categories:** Allow users to select question categories.
- **Database Integration:** Store quiz data in a database instead of a JSON file.
- **Online Quiz:** Implement an online quiz with user authentication and leaderboards.
- **Logging:** Implement a logging system to track quiz attempts and potential errors.
