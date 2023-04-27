import csv

from Patient import Patient

PATH_TO_PATIENTS_FILE = 'ProjectData\patients.txt'


class PatientManager:
    def __init__(self):
        self.patients = []
        self.read_patients_file()

    def read_patients_file(self):
        with open(PATH_TO_PATIENTS_FILE, 'r') as patients_file:
            file_reader = csv.DictReader(patients_file, delimiter='_')

            for line in file_reader:
                patient = Patient(
                    pid=int(line['id']),
                    name=line['Name'],
                    disease=line['Disease'],
                    gender=line['Gender'],
                    age=int(line['Age']))
                self.patients.append(patient)

    def format_patient_info_for_file(self, patient: Patient) -> str:
        return str(patient)

    def enter_patient_info(self, pid=None) -> Patient:
        if pid is None:
            pid = int(input("Enter the patient's PID: "))
        name = input("Enter the patient's name: ")
        disease = input("Enter the patient's disease: ")
        gender = input("Enter the patient's gender: ")
        age = int(input("Enter the patient's age: "))

        return Patient(pid, name, disease, gender, age)

    def search_patient_by_id(self) -> Patient:
        pid = int(input("Enter the patient's PID: "))

        for patient in self.patients:
            if patient.pid == pid:
                print(str(patient))
                return patient

        print("Can't find the patient...")

    def display_patient_info(self, patient):
        print("ID Name Disease Gender Age")
        print(" ".join([str(patient.pid), patient.name, patient.disease, patient.gender, str(patient.age)]))

    def replace_patient(self, patient: Patient):
        index_to_replace = -1

        for p in self.patients:
            if p.pid == patient.pid:
                index_to_replace = self.patients.index(p)

        if index_to_replace != -1:
            self.patients[index_to_replace] = patient

    def edit_patient_info_by_id(self):
        patient = self.search_patient_by_id()

        if patient is not None:
            updated_patient = self.enter_patient_info(patient.pid)
            self.replace_patient(updated_patient)
            self.write_list_of_patients_to_file()
            print('The patient has been edited!')
        else:
            print('Cannot find the patient....')

    def display_patients_list(self):
        print("ID Name Disease Gender Age")
        for patient in self.patients:
            print(" ".join([str(patient.pid), patient.name, patient.disease, patient.gender, str(patient.age)]))


def write_list_of_patients_to_file(self):
    header_line = 'id_Name_Disease_Gender_Age'
    with open(PATH_TO_PATIENTS_FILE, 'w') as patients_file:
        # Adding the header
        patients_file.write(header_line)
        patients_file.write('\n')

        for patient in self.patients:
            patients_file.write(str(patient))
            patients_file.write('\n')


def add_patient_to_file(self):
    new_patient = self.enter_patient_info()
    self.patients.append(new_patient)
    self.write_list_of_patients_to_file()
    print('The patient has been added!')
