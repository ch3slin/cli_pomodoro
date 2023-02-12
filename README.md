# Pomodoro Timer CLI

![](https://img.shields.io/pypi/pyversions/3?style=for-the-badge)


A simple command line interface (CLI) application for the Pomodoro technique. The Pomodoro technique is a time management method used to boost productivity and focus. The technique involves breaking work into intervals, typically 25 minutes in length, separated by short breaks.

## Features
- Allows the user to specify the interval and break time in minutes
- Plays an alarm sound when the interval or break time ends
- Allows the user to specify a custom MP3 file to use as the alarm sound
## Requirements
- Python 3
## Usage
- To run the application, open a terminal window and navigate to the directory containing the pomodoro.py file. Then, run the following command:

```py
python pomodoro.py [-i INTERVAL] [-b BREAK_TIME] [-f FILE_PATH]
```
where:
- -i INTERVAL is the interval time in minutes (default is 25 minutes)
- -b BREAK_TIME is the break time in minutes (default is 5 minutes)
- -f FILE_PATH is the file path to the MP3 file to use as the alarm sound (optional)

## Example
```py
python pomodoro.py -i 30 -b 10 -f /path/to/alarm.mp3
```
This example runs the Pomodoro timer with a 30-minute interval and a 10-minute break, using /path/to/alarm.mp3 as the alarm sound.
