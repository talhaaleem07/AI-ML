class Department:
    def __init__(self, department_id, name):
        self.id = department_id
        self.name = name

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["id"], data["name"])
