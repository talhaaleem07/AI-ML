class Student:
    def __init__(self, student_id, name, roll_number, student_class, contact):
        self.id = student_id
        self.name = name
        self.roll_number = roll_number
        self.student_class = student_class
        self.contact = contact

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "roll_number": self.roll_number,
            "class": self.student_class,
            "contact": self.contact
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["id"],
            data["name"],
            data["roll_number"],
            data["class"],
            data["contact"]
        )
