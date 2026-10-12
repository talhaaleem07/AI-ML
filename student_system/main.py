from manager import StudentManager


manager = StudentManager()


def get_integer(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Please enter a valid whole number.")


def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Please enter a valid number.")


def show_students(students):
    if len(students) == 0:
        print("No students found.")
        return
    for student in students:
        print(f"ID: {student.id}")
        print(f"Name: {student.name}")
        print(f"Roll Number: {student.roll_number}")
        print(f"Class: {student.student_class}")
        print(f"Contact: {student.contact}")
        print("-" * 30)


def add_student():
    print("\nAdd Student")
    name = input("Name: ").strip()
    roll_number = input("Roll number: ").strip()
    student_class = input("Class/grade level: ").strip()
    contact = input("Contact: ").strip()
    student = manager.add_student(name, roll_number, student_class, contact)
    if student is None:
        print("This roll number already exists.")
    else:
        print(f"Student added with ID {student.id}.")


def update_student():
    student_id = get_integer("Student ID to update: ")
    if manager.find_student(student_id) is None:
        print("Student not found.")
        return
    name = input("New name: ").strip()
    roll_number = input("New roll number: ").strip()
    student_class = input("New class/grade level: ").strip()
    contact = input("New contact: ").strip()
    saved, message = manager.update_student(
        student_id, name, roll_number, student_class, contact
    )
    print(message)


def delete_student():
    student_id = get_integer("Student ID to delete: ")
    if manager.delete_student(student_id):
        print("Student and their grades were deleted.")
    else:
        print("Student not found.")


def add_subject():
    subject = manager.add_subject(input("Subject name: ").strip())
    if subject is None:
        print("This subject already exists.")
    else:
        print(f"Subject added with ID {subject.id}.")


def view_subjects():
    subjects = manager.get_subjects()
    if len(subjects) == 0:
        print("No subjects found.")
        return
    for subject in subjects:
        print(f"ID: {subject.id} | Subject: {subject.name}")


def record_grade():
    student_id = get_integer("Student ID: ")
    subject_id = get_integer("Subject ID: ")
    marks_obtained = get_number("Marks obtained: ")
    max_marks = get_number("Maximum marks: ")
    saved, message = manager.record_grade(student_id, subject_id, marks_obtained, max_marks)
    print(message)


def view_student_grades():
    student_id = get_integer("Student ID: ")
    student = manager.find_student(student_id)
    if student is None:
        print("Student not found.")
        return
    grades = manager.student_grades(student_id)
    if len(grades) == 0:
        print("No grades found for this student.")
        return
    print(f"\nGrades for {student.name}")
    for grade in grades:
        subject = manager.find_subject(grade.subject_id)
        percentage = (grade.marks_obtained / grade.max_marks) * 100
        grade_point = manager.grade_point(grade.marks_obtained, grade.max_marks)
        print(f"{subject.name}: {grade.marks_obtained}/{grade.max_marks} | "
              f"{percentage:.2f}% | Grade Point: {grade_point:.1f}")


def calculate_gpa():
    student_id = get_integer("Student ID: ")
    student = manager.find_student(student_id)
    if student is None:
        print("Student not found.")
        return
    gpa = manager.calculate_gpa(student_id)
    if gpa is None:
        print("No grades found for this student.")
    else:
        print(f"GPA for {student.name}: {gpa:.2f}")


def search_students():
    search_text = input("Enter name or roll number to search: ").strip()
    show_students(manager.search_students(search_text))


def filter_by_class():
    student_class = input("Enter class/grade level: ").strip()
    show_students(manager.students_by_class(student_class))


def filter_by_gpa():
    minimum_gpa = get_number("Minimum GPA: ")
    maximum_gpa = get_number("Maximum GPA: ")
    if minimum_gpa > maximum_gpa:
        print("Minimum GPA cannot be greater than maximum GPA.")
        return
    results = manager.students_by_gpa_range(minimum_gpa, maximum_gpa)
    if len(results) == 0:
        print("No students found in this GPA range.")
        return
    for student, gpa in results:
        print(f"{student.name} | Roll No: {student.roll_number} | "
              f"Class: {student.student_class} | GPA: {gpa:.2f}")


def class_performance_report():
    report = manager.class_performance_report()
    if len(report) == 0:
        print("No students found.")
        return
    print("\nClass-wise Performance Report")
    for student_class, average_gpa in report.items():
        print(f"Class {student_class}: Average GPA = {average_gpa:.2f}")


def show_menu():
    print("\n====== Student Management System ======")
    print("1. Add student")
    print("2. View all students")
    print("3. Update student")
    print("4. Delete student")
    print("5. Add subject")
    print("6. View subjects")
    print("7. Record marks/grade")
    print("8. View grades for a student")
    print("9. Calculate student GPA")
    print("10. Search student by name or roll number")
    print("11. Filter students by class")
    print("12. Filter students by GPA range")
    print("13. Class-wise performance report")
    print("0. Exit")


def main():
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_student()
        elif choice == "2":
            show_students(manager.get_students())
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            add_subject()
        elif choice == "6":
            view_subjects()
        elif choice == "7":
            record_grade()
        elif choice == "8":
            view_student_grades()
        elif choice == "9":
            calculate_gpa()
        elif choice == "10":
            search_students()
        elif choice == "11":
            filter_by_class()
        elif choice == "12":
            filter_by_gpa()
        elif choice == "13":
            class_performance_report()
        elif choice == "0":
            print("Goodbye.")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
