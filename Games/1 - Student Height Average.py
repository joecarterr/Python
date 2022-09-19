student_heights = input("Input a list of student heights: ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

total_height = 0
for height in student_heights:
    total_height += height
print(f"This is your total height: {total_height}\n")

number_of_students = 0
for student in student_heights:
    number_of_students += 1  # for loop will run for as many items are in the list so this will add one per added
    # student
print(f"This is your number of students: {number_of_students}\n")

avg_height = total_height / number_of_students
avg_height = round(avg_height)
print(f"The average height of you list is {avg_height}!")
