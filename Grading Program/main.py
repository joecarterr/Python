# all the students scores:
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 44,
    "Neville": 62,
}

# empty list:
student_grades = []

for key in student_scores:
    # getting the score of the student:
    grade = student_scores[key]
    # adding the students score to the student grade list:
    student_grades.append(grade)

for score in student_grades:
    if score in range(91, 101):
        print("Outstanding")
    elif score in range(81, 91):
        print("Exceeds Expectations")
    elif score in range(71, 81):
        print("Acceptable")
    elif score in range(50, 71):
        print("Quite poor")
    else:
        print("Failed")
