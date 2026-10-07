# Student Management System
from datetime import datetime

# List to store student records
students = []

# Function to save students to a file
def save_students():
    try:
        file = open("students.txt", "w")

        for student in students:
            file.write(
                str(student["id"]) + "," +
                student["name"] + "," +
                str(student["age"]) + "," +
                student["course"] + "\n"
            )

        file.close()

        print("Student data saved successfully.")

    except Exception:
        print("Error: Unable to save student data.")

# Function to load students from a file
def load_students():
    try:
        file = open("students.txt", "r")

        for line in file:
            data = line.strip().split(",")

            if len(data) == 4:
                student = {
                    "id": int(data[0]),
                    "name": data[1],
                    "age": int(data[2]),
                    "course": data[3]
                }

                students.append(student)

        file.close()

    except FileNotFoundError:
        print("No previous student data found.")

    except Exception:
        print("Error: Unable to load student data.")

# Function to add a new student
def add_student():
    print("\n--- Add Student ---")

    try:
        student_id = int(input("Enter student ID: "))

        # Check if the student ID already exists
        for student in students:
            if student["id"] == student_id:
                print("Error: This student ID already exists.")
                return

        name = input("Enter student name: ")

        age = int(input("Enter student age: "))

        if age <= 0:
            print("Error: Age must be greater than zero.")
            return

        course = input("Enter course name: ")

        # Check for empty input
        if name.strip() == "" or course.strip() == "":
            print("Error: Name and course cannot be empty.")
            return

        student = {
            "id": student_id,
            "name": name,
            "age": age,
            "course": course
        }

        students.append(student)

        save_students()

        print("Student added successfully.")

    except ValueError:
        print("Error: Please enter valid numbers for ID and age.")

# Function to view all students
def view_students():
    print("\n--- Student List ---")

    if len(students) == 0:
        print("No students found.")

    else:
        for student in students:
            print("ID:", student["id"])
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Course:", student["course"])
            print("--------------------")

# Function to search for a student
def search_student():
    print("\n--- Search Student ---")

    try:
        student_id = int(input("Enter student ID: "))

        found = False

        for student in students:
            if student["id"] == student_id:
                print("Student Found!")
                print("Name:", student["name"])
                print("Age:", student["age"])
                print("Course:", student["course"])

                found = True
                break

        if not found:
            print("Student not found.")

    except ValueError:
        print("Error: Please enter a valid student ID.")

# Function to delete a student
def delete_student():
    print("\n--- Delete Student ---")

    try:
        student_id = int(input("Enter student ID: "))

        for student in students:
            if student["id"] == student_id:
                students.remove(student)

                save_students()

                print("Student deleted successfully.")
                return

        print("Student not found.")

    except ValueError:
        print("Error: Please enter a valid student ID.")

# Load previously saved students
load_students()

# Main program
while True:

    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Save Student Data")
    print("6. Show Current Date and Time")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        save_students()

    elif choice == "6":
        current_time = datetime.now()
        print("Current Date and Time:", current_time)

    elif choice == "7":
        print("Thank you for using Student Management System.")
        break

    else:
        print("Invalid choice. Please select a number from 1 to 7.")