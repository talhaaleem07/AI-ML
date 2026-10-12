class Attendance:
    VALID_STATUSES = ["Present", "Absent", "Leave"]

    def __init__(self, attendance_id, employee_id, date, status):
        self.id = attendance_id
        self.employee_id = employee_id
        self.date = date
        self.status = status

    def to_dict(self):
        return {
            "id": self.id,
            "employee_id": self.employee_id,
            "date": self.date,
            "status": self.status
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["id"],
            data["employee_id"],
            data["date"],
            data["status"]
        )
