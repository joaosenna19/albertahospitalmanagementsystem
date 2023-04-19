# Object-Oriented Programming 1 - CPRG-216-D
# Assignment: Project Classes
# Group 13 - Joao Antonio Senna Alves Radicchi (Tony), Lucas Dayan and Gabriel Gomes
# The following code represents the class DoctorManager, responsible for storing its methods.

import doctor


class DoctorManager:
    # The intention here is to not initialize the parameter with a mutable
    def __init__(self, list_of_doctors=None):
        # value, such as []
        if list_of_doctors is None:
            list_of_doctors = []
        self.list_of_doctors = list_of_doctors
        self.__read_doctors_file('doctors.txt')

    # Private method in order to avoid it to be called outside the class
    def __format_dr_info(self, doctor_obj):
        formatted_doc = f"{doctor_obj.doctor_id}_{doctor_obj.name}_{doctor_obj.specialization}_" \
                        f"{doctor_obj.working_time}_{doctor_obj.qualification}_" \
               f"{doctor_obj.room_number}"
        return formatted_doc

    # Private method in order to avoid it to be called outside the class
    def __enter_dr_info(self):
        doctor_id = int(input("Enter the doctor's ID: ").strip())
        doctor_name = input("Enter the doctor's name: ").strip()
        doctor_speciality = input("Enter the doctor's speciality: ").strip()
        doctor_timing = input("Enter the doctor's timing: ").strip()
        doctor_qualification = input("Enter the doctor's qualification: ").strip()
        doctor_room = int(input("Enter the doctor's room number: ").strip())

        new_doc = doctor.Doctor(doctor_id, doctor_name, doctor_speciality, doctor_timing, doctor_qualification,
                                doctor_room)

        return new_doc

    # Private method in order to avoid it to be called outside the class
    def __read_doctors_file(self, file_name):
        with open(file_name) as file:
            # Jump the heading of the file
            next(file)
            for line in file:
                doc_infos = line.split('_')
                new_doc = doctor.Doctor(doc_infos[0], doc_infos[1], doc_infos[2], doc_infos[3], doc_infos[4],
                                        doc_infos[5])
                self.list_of_doctors.append(new_doc)

    def search_doctor_by_id(self):
        id_searched = input("Enter the doctor ID: ")
        heading = ['Id', 'Name', 'Speciality', 'Timing', 'Qualification', 'Room Number']
        for doc in self.list_of_doctors:
            if doc.doctor_id == id_searched:
                print('{:<5s} {:<20s} {:<15s} {:<10s} {:<15s} {:<10s}'.format(*heading))
                self.display_doctor_info(doc)
                break
        else:
            print("Can't find the doctor with the same ID on the system.")

    def search_doctor_by_name(self):
        name_searched = input("Enter the doctor name: ")
        heading = ['Id', 'Name', 'Speciality', 'Timing', 'Qualification', 'Room Number']
        for doc in self.list_of_doctors:
            if doc.name == name_searched:
                print('{:<5s} {:<20s} {:<15s} {:<10s} {:<15s} {:<10s}'.format(*heading))
                self.display_doctor_info(doc)
                break
        else:
            print("Can't find the doctor with the same name on the system")

    def display_doctor_info(self, doc_obj):
        # Formats according to the output provided
        print('{:<5s} {:<20s} {:<15s} {:<10s} {:<15s} {:<10s}'.format(str(doc_obj.doctor_id), str(doc_obj.name),
                                                                      str(doc_obj.specialization),
                                                                      str(doc_obj.working_time),
                                                                      str(doc_obj.qualification),
                                                                      str(doc_obj.room_number)))

    def edit_doctor_info(self):
        # As the function enter_dr_info asks the user to insert the ID of the doctor, it was required to create a
        # local function in the cases that you don't want the user to provide any ID.
        def enter_dr_info_locally(doctor_id):
            doctor_name = input("Enter new name: ").strip()
            doctor_speciality = input("Enter new speciality: ").strip()
            doctor_timing = input("Enter new timing: ").strip()
            doctor_qualification = input("Enter new qualification: ").strip()
            doctor_room = int(input("Enter new room number: ").strip())

            n_doc = doctor.Doctor(doctor_id, doctor_name, doctor_speciality, doctor_timing, doctor_qualification,
                                  doctor_room)
            return n_doc

        id_to_edit = input("Please enter the id of the doctor that you want to edit their information: ").strip()
        for doc in self.list_of_doctors:
            if doc.doctor_id == id_to_edit:
                new_doc = enter_dr_info_locally(doc.doctor_id)
                index = self.list_of_doctors.index(doc)
                self.list_of_doctors[index] = new_doc
                self.__write_list_of_doctors_to_file()
                print(f"Doctor whose ID is {id_to_edit} has been edited.")
                break
        else:
            print("Can't find the doctor with the same ID on the system.")

    def display_doctors_info(self):
        heading = ['Id', 'Name', 'Speciality', 'Timing', 'Qualification', 'Room Number']
        print('{:<5s} {:<20s} {:<15s} {:<10s} {:<15s} {:<10s}'.format(*heading))
        for doc in self.list_of_doctors:
            self.display_doctor_info(doc)

    # The solution for this part was rewriting the heading of the file every time and then appending all the doctors
    # from the updated list
    # Private method in order to avoid it to be called outside the class
    def __write_list_of_doctors_to_file(self):
        with open('doctors.txt', 'w') as file:
            file.write('id_name_specilist_timing_qualification_roomNb')

        with open('doctors.txt', 'a') as file:
            for d in self.list_of_doctors:
                formatted_doc = self.__format_dr_info(d)
                # rstrip() used to avoid blank spaces or new lines after formatting, a problem that happened
                formatted_doc = formatted_doc.rstrip()
                file.write('\n' + formatted_doc)

    def add_dr_to_file(self):
        new_doc = self.__enter_dr_info()
        self.list_of_doctors.append(new_doc)
        self.__write_list_of_doctors_to_file()
        print(f"Doctor whose ID is {new_doc.doctor_id} has been added.")