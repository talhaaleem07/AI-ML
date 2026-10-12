class Subject:
    def __init__(self, subject_id, name):
        self.id = subject_id
        self.name = name

    def to_dict(self):
        return {"id": self.id, "name": self.name}

    @classmethod
    def from_dict(cls, data):
        return cls(data["id"], data["name"])
