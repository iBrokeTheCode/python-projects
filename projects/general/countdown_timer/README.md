# Countdown Timer

## Description

This project involves creating a command-line that counts down from a specified time. The user should be able to set the duration of the countdown (in seconds, minutes, or hours) and see the remaining time update in real-time.

## Concepts Covered

- Time manipulation (using the `time` module)
- Basic input/output
- Looping and conditional statements

## Potential Modules

- `time` (for time-related functions like `sleep`)
- `argparse` (optional, for command-line argument parsing)

## Example Usage (Command-Line)

```bash
python countdown_timer.py -H 1 -m 15 -s 30 # 01:15:30
python countdown_timer.py -H 1 # 01:00:00
python countdown_timer.py -m 15 # 00:15:00
python countdown_timer.py -s 30 # 00:00:30
```

## Steps

- **Argument Parsing:**

  - Use `argparse` to handle command-line arguments for specifying the countdown duration.

- **Time Calculation:**
  - Calculate the total countdown time in seconds.
- **Countdown Loop:**
  - Use a loop to decrement the remaining time.
  - **Inside the loop:**
    - Display the remaining time in a user-friendly format (e.g., "Minutes:Seconds").
    - Use `time.sleep(1)` to pause for one second.
- **Completion Message:**
  - After the loop finishes, display a message indicating that the countdown is complete.

## Future Improvements

- **GUI:** Create a graphical user interface (GUI) using Tkinter, PyQt, Flet etc.
- **More Flexible Time Input:** Allow users to enter time in various formats (e.g., "1h 30m 15s").
- **Audio/Visual Alerts:** Play a sound or display a visual cue when the countdown finishes.
- **Pause/Resume Functionality:** Add the ability to pause and resume the countdown.
