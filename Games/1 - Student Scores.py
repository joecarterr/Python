student_scores = input("Please enter a list of the students scores: ")
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

highest_score = 0
for score in student_scores:
    if score > highest_score:
        score = highest_score
print(f"The highest score is {highest_score}")
