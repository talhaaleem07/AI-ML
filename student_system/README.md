# Student Management System

A beginner-level terminal project for managing students, subjects, marks, and GPA. It uses JSON files for local storage and does not need a database or external packages.

## Run the program

Open a terminal inside the `student_system` folder and run:

```text
python main.py
```

## Features

1. Add, view, update, and delete students
2. Add and view subjects
3. Record marks for a student and subject
4. View a student's grades
5. Calculate GPA from saved marks
6. Search by name or roll number
7. Filter students by class
8. Filter students by GPA range
9. Show the average GPA for each class
10. Save all information in JSON files

The program automatically creates the `data` folder and these files if they are missing:

- `students.json`
- `subjects.json`
- `grades.json`

## GPA scale

- 90% and above: 4.0
- 80% to 89%: 3.7
- 70% to 79%: 3.3
- 60% to 69%: 3.0
- 50% to 59%: 2.0
- Below 50%: 0.0
