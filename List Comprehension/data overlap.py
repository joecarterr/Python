with open("List Comprehension/file1.txt") as file1:
    readlines1 = file1.readlines()

with open("List Comprehension/file2.txt") as file2:
    readlines2 = file2.readlines()

result = [int(number) for number in readlines1 if number in readlines2]
print(result)

