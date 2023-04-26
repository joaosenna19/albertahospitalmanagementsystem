class Management:
    
    def __init__(self):
        self.doctor_management = doctor_manager()
        self.patient_management = PatientManager()
    
    def display_menu(self):
        print("Welcome to Alberta Hospital (AH) Management system")
        while True:
            print("Select from the following options, or select 3 to stop:")
            print("1 - Doctors")
            print("2 - Patients")
            print("3 - Exit Program")
            choice = input("Enter your choice: ")
            if choice == "1":
                
                while True:
                    
                    print("Select from the following options, or select 6 to return to the main menu:")
                    print("1 - Display doctors list")
                    print("2 - Search doctor by ID")
                    print("3 - Search doctor by name")
                    print("4 - Add a new doctor")
                    print("5 - Edit existing doctor information")
                    print("6 - Return to main menu")
                    
                    doctor_choice = input("Enter your choice: ")
                    if doctor_choice == "1":
                        self.doctor_management.display_doctors()
                    elif doctor_choice == "2":
                        id = input("Enter doctor ID: ")
                        self.doctor_management.search_doctor_by_id(id)
                    elif doctor_choice == "3":
                        name = input("Enter doctor name: ")
                        self.doctor_management.search_doctor_by_name(name)
                    elif doctor_choice == "4":
                        doctor = Doctor()
                        self.doctor_management.add_doctor(doctor)
                    elif doctor_choice == "5":
                        id = input("Enter doctor ID: ")
                        self.doctor_management.edit_doctor_info(id)
                    elif doctor_choice == "6":
                        break
                    else:
                        
                        print("Invalid choice. Please try again.")
                        
            elif choice == "2":
                while True:
                    print("Select from the following options, or select 5 to return to the main menu:")
                    print("1 - Display patients list")
                    print("2 - Search patient by ID")
                    print("3 - Add a new patient")
                    print("4 - Edit existing patient information")
                    print("5 - Return to main menu")
                    patient_choice = input("Enter your choice: ")
                    if patient_choice == "1":
                        self.patient_management.display_patients()
                    elif patient_choice == "2":
                        id = input("Enter patient ID: ")
                        self.patient_management.search_patient_by_id(id)
                    elif patient_choice == "3":
                        patient = Patient()
                        self.patient_management.add_patient(patient)
                    elif patient_choice == "4":
                        id = input("Enter patient ID: ")
                        self.patient_management.edit_patient_info(id)
                    elif patient_choice == "5":
                        break
                    else:
                        print("Invalid choice. Please try again.")
            elif choice == "3":
                break
            else:
                print("Invalid choice. Please try again.")
