#PF-Assgn-32
def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
    # write your logic here
    if patient_medical_speciality_list.count('P') > patient_medical_speciality_list.count('E'):
        if patient_medical_speciality_list.count('P') > patient_medical_speciality_list.count('O'):
            speciality = medical_speciality['P']
        else:
            speciality = medical_speciality['O']
    elif patient_medical_speciality_list.count('E') > patient_medical_speciality_list.count('O'):
        speciality = medical_speciality['E']
    else:
        speciality = medical_speciality['E']
    return speciality

#provide different values in the list and test your program
patient_medical_speciality_list=[301,'P',302, 'P' ,305, 'P' ,401, 'E' ,656, 'E']
medical_speciality={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)