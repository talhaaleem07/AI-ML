import json
import os

from grade import Grade
from student import Student
from subject import Subject


class StudentManager:
    def __init__(self):
        self.data_folder = os.path.join(os.path.dirname(__file__), "data")
        self.student_file = os.path.join(self.data_folder, "students.json")
        self.subject_file = os.path.join(self.data_folder, "subjects.json")
        self.grade_file = os.path.join(self.data_folder, "grades.json")
        self.create_data_files()

    def create_data_files(self):
        os.makedirs(self.data_folder, exist_ok=True)
        for file_path in [self.student_file, self.subject_file, self.grade_file]:
            if not os.path.exists(file_path):
                self.save_data(file_path, [])

    def load_data(self, file_path):
        try:
            with open(file_path, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.save_data(file_path, [])
            return []

    def save_data(self, file_path, data):
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)

    def get_students(self):
        return [Student.from_dict(data) for data in self.load_data(self.student_file)]

    def get_subjects(self):
        return [Subject.from_dict(data) for data in self.load_data(self.subject_file)]

    def get_grades(self):
        return [Grade.from_dict(data) for data in self.load_data(self.grade_file)]

    def get_next_id(self, objects):
        if len(objects) == 0:
            return 1
        return max(item.id for item in objects) + 1

    def find_student(self, student_id):
        for student in self.get_students():
            if student.id == student_id:
                return student
        return None

    def find_subject(self, subject_id):
        for subject in self.get_subjects():
            if subject.id == subject_id:
                return subject
        return None

    def add_student(self, name, roll_number, student_class, contact):
        students = self.get_students()
        for student in students:
            if student.roll_number.lower() == roll_number.lower():
                return None

        student = Student(
            self.get_next_id(students), name, roll_number, student_class, contact
        )
        students.append(student)
        self.save_data(self.student_file, [item.to_dict() for item in students])
        return student

    def update_student(self, student_id, name, roll_number, student_class, contact):
        students = self.get_students()
        for student in students:
            if student.roll_number.lower() == roll_number.lower() and student.id != student_id:
                return False, "Roll number already exists."

        for student in students:
            if student.id == student_id:
                student.name = name
                student.roll_number = roll_number
                student.student_class = student_class
                student.contact = contact
                self.save_data(self.student_file, [item.to_dict() for item in students])
                return True, "Student updated."
        return False, "Student not found."

    def delete_student(self, student_id):
        students = self.get_students()
        for student in students:
            if student.id == student_id:
                students.remove(student)
                self.save_data(self.student_file, [item.to_dict() for item in students])
                grades = [grade for grade in self.get_grades() if grade.student_id != student_id]
                self.save_data(self.grade_file, [item.to_dict() for item in grades])
                return True
        return False

    def add_subject(self, name):
        subjects = self.get_subjects()
        for subject in subjects:
            if subject.name.lower() == name.lower():
                return None
        subject = Subject(self.get_next_id(subjects), name)
        subjects.append(subject)
        self.save_data(self.subject_file, [item.to_dict() for item in subjects])
        return subject

    def record_grade(self, student_id, subject_id, marks_obtained, max_marks):
        if self.find_student(student_id) is None:
            return False, "Student not found."
        if self.find_subject(subject_id) is None:
            return False, "Subject not found."
        if max_marks <= 0 or marks_obtained < 0 or marks_obtained > max_marks:
            return False, "Marks must be between 0 and maximum marks."

        grades = self.get_grades()
        for grade in grades:
            if grade.student_id == student_id and grade.subject_id == subject_id:
                grade.marks_obtained = marks_obtained
                grade.max_marks = max_marks
                self.save_data(self.grade_file, [item.to_dict() for item in grades])
                return True, "Grade updated."

        grades.append(Grade(student_id, subject_id, marks_obtained, max_marks))
        self.save_data(self.grade_file, [item.to_dict() for item in grades])
        return True, "Grade saved."

    def student_grades(self, student_id):
        return [grade for grade in self.get_grades() if grade.student_id == student_id]

    def grade_point(self, marks_obtained, max_marks):
        percentage = (marks_obtained / max_marks) * 100
        if percentage >= 90:
            return 4.0
        elif percentage >= 80:
            return 3.7
        elif percentage >= 70:
            return 3.3
        elif percentage >= 60:
            return 3.0
        elif percentage >= 50:
            return 2.0
        return 0.0

    def calculate_gpa(self, student_id):
        grades = self.student_grades(student_id)
        if len(grades) == 0:
            return None
        total_points = 0
        for grade in grades:
            total_points += self.grade_point(grade.marks_obtained, grade.max_marks)
        return total_points / len(grades)

    def search_students(self, search_text):
        search_text = search_text.lower()
        results = []
        for student in self.get_students():
            if search_text in student.name.lower() or search_text in student.roll_number.lower():
                results.append(student)
        return results

    def students_by_class(self, student_class):
        return [student for student in self.get_students()
                if student.student_class.lower() == student_class.lower()]

    def students_by_gpa_range(self, minimum_gpa, maximum_gpa):
        results = []
        for student in self.get_students():
            gpa = self.calculate_gpa(student.id)
            if gpa is not None and minimum_gpa <= gpa <= maximum_gpa:
                results.append((student, gpa))
        return results

    def class_performance_report(self):
        report = {}
        for student in self.get_students():
            if student.student_class not in report:
                report[student.student_class] = []
            gpa = self.calculate_gpa(student.id)
            if gpa is not None:
                report[student.student_class].append(gpa)

        averages = {}
        for student_class, gpas in report.items():
            if len(gpas) == 0:
                averages[student_class] = 0
            else:
                averages[student_class] = sum(gpas) / len(gpas)
        return averages
