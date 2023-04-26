class Patient:
    def __init__(self, pid: int = None, name: str = None, disease: str = None, gender: str = None, age: int = None):
        self.pid: int = pid
        self.name: str = name
        self.disease: str = disease
        self.gender: str = gender
        self.age: int = age

    def __str__(self):
        return '_'.join([str(self.pid),
                         self.name,
                         self.disease,
                         self.gender,
                         str(self.age)])
