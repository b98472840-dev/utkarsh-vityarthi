# Project Report: Class Attendance Tracker

**Name:** Naitik Mishra
**Course:** Python Programming, 1st Semester
**University:** VIT Bhopal
**Project file:** `cat_2.py`

---

## 1. Introduction

Taking attendance by hand is slow and it is easy to make mistakes. In this project I made a small terminal program in Python that takes attendance one student at a time and makes the report by itself. I chose this project because it uses many basic Python topics that we studied in class, and it is also something useful in real life.

## 2. Objectives

- Practise lists, dictionaries, loops and conditions
- Learn how to read input from the user and check it
- Learn how to write data into a file
- Build a program that is easy to use and does not crash on wrong input

## 3. Tools and Requirements

| Item | Detail |
|---|---|
| Language | Python 3.8 or newer |
| Modules | `os`, `time`, `datetime` (all built in) |
| Platform | Windows, Linux or Mac terminal |
| Output | Screen summary and `.txt` report |

## 4. Working of the Program

**Step 1: Main menu.** The program shows a banner and two options: start attendance or exit.

**Step 2: Student loop.** Students are stored in a list called `students`. Each student is a dictionary with a `roll` and a `name`. A `while` loop with an index `i` shows one student at a time.

**Step 3: Marking.** The user types one key:

- `p` adds the student to the present list
- `a` adds the student to the absent list
- `l` adds the student to the late list
- `b` goes back to the previous student

Any other key shows an error and asks again.

**Step 4: Undo feature.** Every mark is also saved in a list called `history`. When the user presses `b`, the last item of `history` is removed, the student is removed from the matching list, and `i` is reduced by 1. If the user is on the first student, the program says that going back is not possible.

**Step 5: Summary.** After the last student, the program counts the lists and finds the percentage:

```
percentage = ((present + late) / total) * 100
```

**Step 6: Report file.** The program creates a file named with the current date and time and writes the counts and the list of students in each group. A `try` and `except` block handles any file error.

## 5. Concepts Used

| Concept | Where it is used |
|---|---|
| List of dictionaries | Storing student data |
| `while` loop | Menu and student loop |
| `if / elif / else` | Checking the key pressed |
| `datetime` | Session time and file name |
| f-strings | Formatting output |
| File handling | Saving the report |
| `try / except` | Handling file write errors |
| ANSI colour codes | Coloured text in the terminal |

## 6. Sample Output

```
ATTENDANCE SUMMARY
  Total Strength : 7
  Total Present  : 5
  Total Absent   : 1
  Late Aaye Bache: 1
  Attendance %   : 85.71%
```

## 7. Limitations

- The student list is fixed inside the code
- Late students are counted as present
- The report is saved only as a text file
- Only one class can be handled at a time
- Emojis may not display on some old Windows consoles

## 8. Future Scope

- Read the student list from a CSV file
- Store the attendance of many days and find the monthly percentage
- Warn about students who have less than 75% attendance
- Add a simple login for the teacher
- Make a small GUI version

## 9. Conclusion

This project helped me understand how basic Python concepts work together in a real program. I learned how loops, lists and files can be combined, and how an undo option can be made using a history list. The program is simple but it works, and it can be improved further in the future.
