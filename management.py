import doctor_manager
import PatientManager


class Management:

    def __init__(self):
        self.doctor_management = doctor_manager.DoctorManager()
        self.patient_management = PatientManager.PatientManager()

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
                        self.doctor_management.display_doctors_info()
                    elif doctor_choice == "2":
                        self.doctor_management.search_doctor_by_id()
                    elif doctor_choice == "3":
                        self.doctor_management.search_doctor_by_name()
                    elif doctor_choice == "4":
                        self.doctor_management.add_dr_to_file()
                    elif doctor_choice == "5":
                        self.doctor_management.edit_doctor_info()
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
                        self.patient_management.display_patients_list()
                    elif patient_choice == "2":
                        self.patient_management.search_patient_by_id()
                    elif patient_choice == "3":
                        self.patient_management.add_patient_to_file()
                    elif patient_choice == "4":
                        self.patient_management.edit_patient_info_by_id()
                    elif patient_choice == "5":
                        break
                    else:
                        print("Invalid choice. Please try again.")
            elif choice == "3":
                break
            else:
                print("Invalid choice. Please try again.")
