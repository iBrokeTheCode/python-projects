# Simple Alarm Clock CLI

## Description

This project involves creating a command-line alarm clock. The user will be able to set an alarm for a specific time (in HH:MM format, 24-hour clock). When the current time matches the set alarm time, the program will play a sound or display a notification.

## Concepts Covered

- Command-line argument parsing
- Working with time and dates in Python
- Basic input/output
- Potentially playing sound on the system (platform-dependent)
- Looping and time comparison

## Potential Modules

- `argparse` (for handling command-line arguments)
- `time` (for working with time-related functions)
- `datetime` (for more advanced date and time manipulation, though `time` might suffice for this simple case)
- `playsound` (for playing sound files - requires installation: `pip install playsound`) or other platform-specific sound libraries.

## Example Usage

```bash
python alarm_clock.py --time 07:30
python alarm_clock.py -t 14:45
```

## Steps

- [ ] **Argument Parsing:**

  - Use argparse to handle the following command-line argument:
  - --time or -t: The alarm time in HH:MM format (string, required). You'll need to validate this format.

- [ ] **Time Validation:**

  Implement a function to validate that the provided time string is in the correct HH:MM format and represents a valid time (00:00 to 23:59).

- [ ] **Getting the Current Time:**

  Use the time module (e.g., time.localtime(), time.strftime()) to get the current time.

- [ ] **Alarm Loop:**

  - Create a loop that continuously checks the current time against the set alarm time.
  - Inside the loop, you'll need to pause for a short interval (e.g., 1 second) to avoid excessive CPU usage (time.sleep()).

- [ ] **Alarm Trigger:**

  - When the current time matches the set alarm time, trigger the alarm action. This could involve:
  - Printing a message to the console.
  - Playing a sound file using the playsound module (or a platform-specific alternative). Note: Playing sound can be platform-dependent and might require additional setup. For simplicity in the initial version, just printing a message is recommended.

- [ ] **Exiting the Alarm:**

  Consider how the alarm program should exit after the alarm is triggered (e.g., run once and exit, or allow the user to set another alarm). For a simple version, exiting after triggering once is sufficient.

- [ ] **Error Handling:**

  - Handle cases where the user provides an invalid time format.
  - Consider potential errors with sound playback if you implement that feature.

## Future Improvements

- **Sound Selection:** Allow the user to specify a sound file to play.
- **Snooze Functionality:** Implement a snooze option.
- **Multiple Alarms:** Allow setting multiple alarms.
- **Recurring Alarms:** Implement the ability to set alarms for specific days of the week.
- **GUI:** Create a graphical user interface for the alarm clock.
