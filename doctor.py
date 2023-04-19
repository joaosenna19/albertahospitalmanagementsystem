# Object-Oriented Programming 1 - CPRG-216-D
# Assignment: Project Classes
# Group 13 - Joao Antonio Senna Alves Radicchi (Tony), Lucas Dayan and Gabriel Gomes
# The following code represents the class Doctor, responsible for storing its properties and methods.

class Doctor:
    def __init__(self, doctor_id=None, name=None, specialization=None, working_time=None, qualification=None,
                 room_number=None):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.working_time = working_time
        self.qualification = qualification
        self.room_number = room_number

    @property
    def doctor_id(self):
        return self._doctor_id

    @doctor_id.setter
    def doctor_id(self, value):
        self._doctor_id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def specialization(self):
        return self._specialization

    @specialization.setter
    def specialization(self, value):
        self._specialization = value

    @property
    def working_time(self):
        return self._working_time

    @working_time.setter
    def working_time(self, value):
        self._working_time = value

    @property
    def qualification(self):
        return self._qualification

    @qualification.setter
    def qualification(self, value):
        self._qualification = value

    @property
    def room_number(self):
        return self._room_number

    @room_number.setter
    def room_number(self, value):
        self._room_number = value

    def __str__(self):
        return f"{self.doctor_id}_{self.name}_{self.specialization}_{self.working_time}_{self.qualification}_" \
               f"{self.room_number}"
