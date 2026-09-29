# Problem Statement

## Title
Class Attendance Tracker in Python

## Description
Python terminal tool for class attendance.

## Problem
In many classes, attendance is taken on paper or by calling names out loud. This takes time, and mistakes happen: a wrong tick, a lost sheet, or a wrong percentage when it is counted by hand.

## Objective
To build a simple program that:

1. Shows each student's roll number and name one by one
2. Lets the teacher mark Present, Absent or Late with a single key
3. Lets the teacher go back and correct a wrong entry
4. Calculates the attendance percentage automatically
5. Saves the final report in a text file

## Scope
The project works for one class with a fixed list of students. It runs in the terminal and needs no internet or extra library.

## Tools Used
- Language: Python 3
- Modules: `os`, `time`, `datetime`
- Concepts: lists, dictionaries, loops, conditions, file handling, exception handling

## Expected Output
A summary on the screen and a report file such as `Attendance_Log_<date>_<time>.txt` with the names of present, absent and late students.
