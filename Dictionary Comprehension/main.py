import random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

# student_scores = {new_key: new_value for item in list} :
students_scores = {name:random.randint(1, 100) for name in names}

# passed_students = {new_key:new_value for (key, value) in dictionary.items() if test} :
passed_students = {name:score for (name, score) in students_scores.items() if score >= 60}
failed_students = {name:score for (name, score) in students_scores.items() if score < 60}
print(f"These students passed: {passed_students}")
print(f"These students failed: {failed_students}")
