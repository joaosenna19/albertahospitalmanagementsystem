from Patient import Patient
from PatientManager import PatientManager

if __name__ == '__main__':
    my_manager = PatientManager()

    lucas = Patient(
        pid=2502,
        name='Lucas',
        disease='Flu',
        gender='Male',
        age=29
    )

    # test adding a patient to patients.txt
    # patient_manager.add_patient_to_file()

    print('Testing format patient info for file:')
    print(my_manager.format_patient_info_for_file(lucas))

    print('Testing edit patient info by id:')
    my_manager.edit_patient_info_by_id()

    print('Testing display patients list:')
    my_manager.display_patients_list()

    # All functions are tested transitively by calling the ones above
