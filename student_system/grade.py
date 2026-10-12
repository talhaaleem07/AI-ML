class Grade:
    def __init__(self, student_id, subject_id, marks_obtained, max_marks):
        self.student_id = student_id
        self.subject_id = subject_id
        self.marks_obtained = marks_obtained
        self.max_marks = max_marks

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "subject_id": self.subject_id,
            "marks_obtained": self.marks_obtained,
            "max_marks": self.max_marks
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["student_id"],
            data["subject_id"],
            data["marks_obtained"],
            data["max_marks"]
        )
