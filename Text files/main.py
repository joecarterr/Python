with open("Text files/my_file.txt", "a") as file:
    file.write("\nI am 16 years old")

with open("Text files/my_file.txt") as file:
    contents = file.read()
    print(contents)
