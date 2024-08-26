
# Student Grades Management System

## Description

This is a simple command-line application for managing student grades. It allows you to add, update, delete, display student grades, and save or show the data from a CSV file.

## Features

- **Add Student**: Add a student with a specific grade.
- **Update Student**: Update the grade of an existing student.
- **Delete Student**: Remove a student from the records.
- **Display All Students**: Display all students and their grades in a tabulated format.
- **Save to File**: Save the student data to a CSV file.
- **Show from File**: Display the student data from the CSV file.

## Usage

1. Navigate to the project directory.
2. Run the script using Python.

```sh
python student_grades_management_system.py
```

3. Follow the on-screen instructions to use the application.

## Functions

### `add_students(name, grade)`

Adds a student with the given name and grade to the system.

### `update_students(name, grade)`

Updates the grade of the specified student.

### `delete_students(name)`

Deletes the specified student from the system.

### `display()`

Displays all students and their grades.

### `file_format()`

Saves the student data to a CSV file.

### `show()`

Displays the student data from the CSV file.

## Running Tests

To run the tests, use `pytest`. Ensure you have pytest installed:

```sh
pip install pytest
```

Then, navigate to the project directory and run:

```sh
pytest test_student_grades.py
```

## Requirements

- Python 3.x
- `tabulate` library
- `pytest` library for testing

Install the required libraries using pip:

```sh
pip install tabulate pytest
```

## Author

- **Akshara Rathore**
  - edX username: akshararathore
  - City: Gwalior, Madhya Pradesh
  - Country: India
```

