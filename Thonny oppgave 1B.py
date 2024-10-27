

# Mock data for studenter og idretter
students = ['Preben', 'Truls', 'Andy', 'Mathias', 'Sara', 'Richard', 'Rikke', 'Adelin']
sports = ['Fotball', 'Håndball', 'Golf', 'Innebandy', 'Bryting']

# Fordeler studenter til idretter
student_sports = {
    'Student': students,
    'Idrett': [sports[i % len(sports)] for i in range(len(students))]
}
# Finn idrett for student
# Arguments: Student_navn(str) : navn på studenten
# Returns : idretten studenten hører til, eller "none" hvis studenten ikke hører til noen

# Funksjon for å finne ut hvilken idrett en student hører til
def finn_idrett_for_student(student_navn): 
    for i, student in enumerate(students):
        if student == student_navn:
            return sports[i % len(sports)]
    return None

# Tester funksjonen
print(finn_idrett_for_student('Preben'))# Output: Fotball
print(finn_idrett_for_student('Sara'))    # Output: Bryting
print(finn_idrett_for_student('Richard'))
print(finn_idrett_for_student('Rikke'))
print(finn_idrett_for_student('Mathias'))
print(finn_idrett_for_student('roger'))



