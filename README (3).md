# Class Attendance Tracker

A small Python program that runs in the terminal and helps take class attendance quickly. It shows one student at a time, and you press a key to mark them present, absent or late. At the end it prints a summary and saves a report as a text file.

## Features

- Shows students one by one with their roll number and name
- Keys: `p` = Present, `a` = Absent, `l` = Late, `b` = go Back
- Back option undoes the last entry if you press a wrong key
- Coloured text in the terminal to make it easy to read
- Summary at the end: total, present, absent, late and attendance percentage
- Saves a report file named like `Attendance_Log_2026-09-30_10-15.txt`

## Requirements

- Python 3.8 or newer
- No extra libraries needed (only `os`, `time` and `datetime`, which come with Python)

## How to run

```
python cat_2.py
```

Then choose `1` to start attendance or `2` to exit.

## How it works

1. The student list is stored in a Python list of dictionaries (`roll` and `name`).
2. A `while` loop goes through the list using an index `i`.
3. Every key press is saved in a `history` list. When `b` is pressed, the last entry is removed from history and from the matching list, and `i` goes back by one.
4. After the last student, the program counts each list and calculates the percentage.
5. The report is written to a `.txt` file in the same folder.

## Sample report

```
OFFICIAL CLASS ATTENDANCE REPORT - 2026-09-30_10-15

Present: 5
Absent: 1
Late: 1
Percentage: 85.71%
```

## Limitations

- Students are typed directly in the code, so the list cannot be changed while the program runs
- Late students are counted as present in the percentage
- Emojis may not show properly on some old Windows consoles

## Future ideas

- Load students from a CSV file
- Keep attendance history of many days
- Show which students are below 75% attendance

## Author

Naitik Mishra, 1st semester, VIT Bhopal
