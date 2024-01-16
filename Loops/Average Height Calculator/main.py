global average_height
total = 0
number_of_students = 0

student_heights = input("Please enter a list of students heights: ").split()
for height in range(0, len(student_heights)):
    number_of_students += 1
    total += int(student_heights[height])
    average_height = int(total / number_of_students)
print(average_height)
