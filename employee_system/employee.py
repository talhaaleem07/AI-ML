class Employee:
    def __init__(self, employee_id, name, designation, department, salary, joining_date, contact):
        self.id = employee_id
        self.name = name
        self.designation = designation
        self.department = department
        self.salary = salary
        self.joining_date = joining_date
        self.contact = contact

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "designation": self.designation,
            "department": self.department,
            "salary": self.salary,
            "joining_date": self.joining_date,
            "contact": self.contact
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["id"],
            data["name"],
            data["designation"],
            data.get("department", ""),
            data["salary"],
            data["joining_date"],
            data["contact"]
        )
