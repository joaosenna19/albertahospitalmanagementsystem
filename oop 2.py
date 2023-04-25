def display_menu():
    print("Main Menu")
    print("1. Doctors")
    print("2. Patients")
    print("3. Exit")

def display_doctors_menu():
    print("Doctors Menu")
    print("1. Display doctors list")
    print("2. Search doctor by ID")
    print("3. Search doctor by name")
    print("4. Add new doctor")
    print("5. Edit doctor information")
    print("6. Return to main menu")

def display_patients_menu():
    print("Patients Menu")
    print("1. Display patients list")
    print("2. Search patient by ID")
    print("3. Add new patient")
    print("4. Edit patient information")
    print("5. Return to main menu")

def display_doctors_list(doctors_list):
    print("Doctor ID | Name\t | Specialist | Timing \t\t | Qualification | Room No.")
    print("-" * 85)
    for doctor in doctors_list:
        print(doctor)

def search_doctor_by_id(doctors_list, doctor_id):
    for doctor in doctors_list:
        if doctor[0] == doctor_id:
            print("Doctor found!")
            print("Doctor ID | Name\t | Specialist | Timing \t\t | Qualification | Room No.")
            print("-" * 85)
            print(doctor)
            return
    print("Doctor not found!")

def search_doctor_by_name(doctors_list, doctor_name):
    found = False
    for doctor in doctors_list:
        if doctor[1].lower() == doctor_name.lower():
            found = True
            print("Doctor found!")
            print("Doctor ID | Name\t | Specialist | Timing \t\t | Qualification | Room No.")
            print("-" * 85)
            print(doctor)
    if not found:
        print("Doctor not found!")

def add_new_doctor(doctors_list):
    doctor_id = input("Enter doctor ID: ")
    for doctor in doctors_list:
        if doctor[0] == doctor_id:
            print("Doctor with this ID already exists!")
            return
    name = input("Enter doctor name: ")
    specialist = input("Enter doctor specialist: ")
    timing = input("Enter doctor timing: ")
    qualification = input("Enter doctor qualification: ")
    room_no = input("Enter doctor room number: ")
    doctors_list.append((doctor_id, name, specialist, timing, qualification, room_no))
    print("Doctor added successfully!")

def edit_doctor_information(doctors_list):
    doctor_id = input("Enter doctor ID: ")
    for i, doctor in enumerate(doctors_list):
        if doctor[0] == doctor_id:
            print("Doctor found!")
            name = input("Enter new name or press enter to keep the current name: ")
            specialist = input("Enter new specialist or press enter to keep the current specialist: ")
            timing = input("Enter new timing or press enter to keep the current timing: ")
            qualification = input("Enter new qualification or press enter to keep the current qualification: ")
            room_no = input("Enter new room number or press enter to keep the current room number: ")
            doctors_list[i] = (doctor_id, name if name else doctor[1], specialist if specialist else doctor[2], timing if timing else doctor[3], qualification if qualification else doctor[4], room_no if room_no else doctor[5])
            print("Doctor information updated successfully!")
            return
    print("Doctor not found!")

def display_patients_list(patients_list):
    print("Patient ID | Name\t | Age | Gender | Phone No.")
