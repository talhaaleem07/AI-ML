import json
import os

from attendance import Attendance
from department import Department
from employee import Employee


class EmployeeManager:
    def __init__(self):
        self.data_folder = os.path.join(os.path.dirname(__file__), "data")
        self.employee_file = os.path.join(self.data_folder, "employees.json")
        self.department_file = os.path.join(self.data_folder, "departments.json")
        self.attendance_file = os.path.join(self.data_folder, "attendance.json")
        self.create_data_files()

    def create_data_files(self):
        os.makedirs(self.data_folder, exist_ok=True)
        for file_path in [self.employee_file, self.department_file, self.attendance_file]:
            if not os.path.exists(file_path):
                self.save_data(file_path, [])

    def load_data(self, file_path):
        try:
            with open(file_path, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def save_data(self, file_path, data):
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)

    def get_employees(self):
        employee_data = self.load_data(self.employee_file)
        return [Employee.from_dict(data) for data in employee_data]

    def get_departments(self):
        department_data = self.load_data(self.department_file)
        return [Department.from_dict(data) for data in department_data]

    def get_attendance(self):
        attendance_data = self.load_data(self.attendance_file)
        return [Attendance.from_dict(data) for data in attendance_data]

    def get_next_id(self, objects):
        if len(objects) == 0:
            return 1
        return max(item.id for item in objects) + 1

    def add_employee(self, name, designation, salary, joining_date, contact):
        employees = self.get_employees()
        employee_id = self.get_next_id(employees)
        employee = Employee(
            employee_id,
            name,
            designation,
            "Unassigned",
            salary,
            joining_date,
            contact
        )
        employees.append(employee)
        self.save_data(self.employee_file, [item.to_dict() for item in employees])
        return employee

    def update_employee(self, employee_id, name, designation, salary, joining_date, contact):
        employees = self.get_employees()
        employee = self.find_employee(employee_id)
        if employee is None:
            return False

        employee.name = name
        employee.designation = designation
        employee.salary = salary
        employee.joining_date = joining_date
        employee.contact = contact
        self.save_data(self.employee_file, [item.to_dict() for item in employees])
        return True

    def delete_employee(self, employee_id):
        employees = self.get_employees()
        employee = self.find_employee(employee_id)
        if employee is None:
            return False

        employees.remove(employee)
        self.save_data(self.employee_file, [item.to_dict() for item in employees])
        attendance = [item for item in self.get_attendance() if item.employee_id != employee_id]
        self.save_data(self.attendance_file, [item.to_dict() for item in attendance])
        return True

    def find_employee(self, employee_id):
        for employee in self.get_employees():
            if employee.id == employee_id:
                return employee
        return None

    def add_department(self, name):
        departments = self.get_departments()
        department_id = self.get_next_id(departments)
        department = Department(department_id, name)
        departments.append(department)
        self.save_data(self.department_file, [item.to_dict() for item in departments])
        return department

    def assign_department(self, employee_id, department_id):
        employee = self.find_employee(employee_id)
        departments = self.get_departments()
        department = None
        for item in departments:
            if item.id == department_id:
                department = item
                break

        if employee is None or department is None:
            return False

        employees = self.get_employees()
        for item in employees:
            if item.id == employee_id:
                item.department = department.name
                break
        self.save_data(self.employee_file, [item.to_dict() for item in employees])
        return True

    def mark_attendance(self, employee_id, date, status):
        if self.find_employee(employee_id) is None:
            return False, "Employee not found."
        if status not in Attendance.VALID_STATUSES:
            return False, "Status must be Present, Absent, or Leave."

        attendance_list = self.get_attendance()
        for item in attendance_list:
            if item.employee_id == employee_id and item.date == date:
                item.status = status
                self.save_data(self.attendance_file, [record.to_dict() for record in attendance_list])
                return True, "Attendance updated."

        attendance_id = self.get_next_id(attendance_list)
        attendance = Attendance(attendance_id, employee_id, date, status)
        attendance_list.append(attendance)
        self.save_data(self.attendance_file, [item.to_dict() for item in attendance_list])
        return True, "Attendance saved."

    def attendance_history(self, employee_id):
        records = self.get_attendance()
        return [item for item in records if item.employee_id == employee_id]

    def attendance_percentage(self, employee_id):
        records = self.attendance_history(employee_id)
        if len(records) == 0:
            return 0
        present_days = 0
        for record in records:
            if record.status == "Present":
                present_days += 1
        return (present_days / len(records)) * 100

    def calculate_salary(self, employee_id, bonus, deductions):
        employee = self.find_employee(employee_id)
        if employee is None:
            return None
        return employee.salary + bonus - deductions

    def salary_report(self, bonus, deductions):
        report = {}
        for employee in self.get_employees():
            salary = employee.salary + bonus - deductions
            if employee.department not in report:
                report[employee.department] = 0
            report[employee.department] += salary
        return report
