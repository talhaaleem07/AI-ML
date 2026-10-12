from datetime import datetime

from manager import EmployeeManager

manager = EmployeeManager()

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


def get_date(message):
    while True:
        date_text = input(message)
        try:
            datetime.strptime(date_text, "%Y-%m-%d")
            return date_text
        except ValueError:
            print("Use this date format: YYYY-MM-DD")


def show_employees():
    employees = manager.get_employees()
    if len(employees) == 0:
        print("No employees found.")
        return

    print("\nEmployee Records")
    for employee in employees:
        print(f"ID: {employee.id}")
        print(f"Name: {employee.name}")
        print(f"Designation: {employee.designation}")
        print(f"Department: {employee.department}")
        print(f"Salary: {employee.salary:.2f}")
        print(f"Joining Date: {employee.joining_date}")
        print(f"Contact: {employee.contact}")
        print("-" * 30)


def add_employee():
    print("\nAdd Employee")
    name = input("Name: ")
    designation = input("Designation: ")
    salary = get_number("Base salary: ")
    joining_date = get_date("Joining date (YYYY-MM-DD): ")
    contact = input("Contact: ")
    employee = manager.add_employee(name, designation, salary, joining_date, contact)
    print(f"Employee added with ID {employee.id}.")


def update_employee():
    employee_id = get_integer("Enter employee ID to update: ")
    employee = manager.find_employee(employee_id)
    if employee is None:
        print("Employee not found.")
        return

    print("Enter the new information.")
    name = input("Name: ")
    designation = input("Designation: ")
    salary = get_number("Base salary: ")
    joining_date = get_date("Joining date (YYYY-MM-DD): ")
    contact = input("Contact: ")
    manager.update_employee(employee_id, name, designation, salary, joining_date, contact)
    print("Employee updated.")


def delete_employee():
    employee_id = get_integer("Enter employee ID to delete: ")
    if manager.delete_employee(employee_id):
        print("Employee deleted.")
    else:
        print("Employee not found.")


def show_departments():
    departments = manager.get_departments()
    if len(departments) == 0:
        print("No departments found.")
        return

    print("\nDepartments")
    for department in departments:
        print(f"ID: {department.id} | Name: {department.name}")


def add_department():
    name = input("Department name: ")
    department = manager.add_department(name)
    print(f"Department added with ID {department.id}.")


def assign_department():
    show_employees()
    employee_id = get_integer("Enter employee ID: ")
    show_departments()
    department_id = get_integer("Enter department ID: ")
    if manager.assign_department(employee_id, department_id):
        print("Employee assigned to department.")
    else:
        print("Employee or department not found.")


def mark_attendance():
    employee_id = get_integer("Employee ID: ")
    date = get_date("Date (YYYY-MM-DD): ")
    status = input("Status (Present/Absent/Leave): ").strip().title()
    saved, message = manager.mark_attendance(employee_id, date, status)
    print(message)


def view_attendance():
    employee_id = get_integer("Employee ID: ")
    if manager.find_employee(employee_id) is None:
        print("Employee not found.")
        return

    records = manager.attendance_history(employee_id)
    print("\nAttendance History")
    if len(records) == 0:
        print("No attendance records found.")
    else:
        for record in records:
            print(f"{record.date}: {record.status}")
    print(f"Attendance percentage: {manager.attendance_percentage(employee_id):.2f}%")


def calculate_salary():
    employee_id = get_integer("Employee ID: ")
    bonus = get_number("Bonus: ")
    deductions = get_number("Deductions: ")
    salary = manager.calculate_salary(employee_id, bonus, deductions)
    if salary is None:
        print("Employee not found.")
    else:
        print(f"Final salary: {salary:.2f}")


def show_salary_report():
    bonus = get_number("Bonus for each employee: ")
    deductions = get_number("Deductions for each employee: ")
    report = manager.salary_report(bonus, deductions)
    if len(report) == 0:
        print("No employees found.")
        return

    print("\nDepartment-wise Salary Report")
    for department, total_salary in report.items():
        print(f"{department}: {total_salary:.2f}")


def show_menu():
    print("\n========== Employee Management System ==========")
    print("1. Add employee")
    print("2. View employees")
    print("3. Update employee")
    print("4. Delete employee")
    print("5. Add department")
    print("6. View departments")
    print("7. Assign employee to department")
    print("8. Mark daily attendance")
    print("9. View attendance history and percentage")
    print("10. Calculate employee salary")
    print("11. Department-wise salary report")
    print("0. Exit")


def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            show_employees()
        elif choice == "3":
            update_employee()
        elif choice == "4":
            delete_employee()
        elif choice == "5":
            add_department()
        elif choice == "6":
            show_departments()
        elif choice == "7":
            assign_department()
        elif choice == "8":
            mark_attendance()
        elif choice == "9":
            view_attendance()
        elif choice == "10":
            calculate_salary()
        elif choice == "11":
            show_salary_report()
        elif choice == "0":
            print("Goodbye.")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
