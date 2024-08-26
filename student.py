import csv
from tabulate import tabulate


student_grades = {}

# Add student
def add_students(name, grade):
    student_grades[name] = grade
    print(f"Added {name} with a grade of {grade}")

# Update student
def update_students(name, grade):
    if name in student_grades:
        student_grades[name] = grade
        print(f"Updated {name} with a grade of {grade}")
    else:
        print(f"{name} is not found")

# Delete student
def delete_students(name):
    if name in student_grades:
        del student_grades[name]
        print(f"{name} has been successfully deleted")
    else:
        print(f"{name} is not found")

# Display all students
def display():
    if student_grades:
        table = [[name, grade] for name, grade in student_grades.items()]
        print(tabulate(table, headers=["Name", "Grade"], tablefmt="grid"))
    else:
        print("No students found")

# Save to file
def file_format():
    with open("students.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Grade"])
        for name, grade in student_grades.items():
            writer.writerow([name, grade])
    print("Students data has been written to students.csv")

# Show from file
def show():
    try:
        with open("students.csv", newline='') as file:
            reader = csv.reader(file)
            table = list(reader)
            if table:
                print(tabulate(table, headers="firstrow", tablefmt="grid"))
            else:
                print("The file students.csv is empty.")
    except FileNotFoundError:
        print("The file students.csv does not exist.")

# Main function
def main():
    print('\nStudent Grades Management System')
    print("1. Add Student")
    print("2. Update Student")
    print("3. Delete Student")
    print("4. Display all Students")
    print("5. Save to file")
    print("6. Show from file")
    print("7. Exit")

    while True:
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice, please enter a number.")
            continue

        if choice == 1:
            name = input("Enter student name: ")
            try:
                grade = int(input("Enter grade: "))
            except ValueError:
                print("Invalid grade, please enter a number.")
                continue
            add_students(name, grade)
        elif choice == 2:
            name = input("Enter student name: ")
            try:
                grade = int(input("Enter grade: "))
            except ValueError:
                print("Invalid grade, please enter a number.")
                continue
            update_students(name, grade)
        elif choice == 3:
            name = input("Enter student name: ")
            delete_students(name)
        elif choice == 4:
            display()
        elif choice == 5:
            file_format()
        elif choice == 6:
            show()
        elif choice == 7:
            print("Closing the system")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
