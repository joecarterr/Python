programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Hello" : "A greeting to a person"
}

empty_dictionary = {}

empty_dictionary["Loop"] = "The action of doing something over and over again"
print(programming_dictionary["Bug"])
print(empty_dictionary)

# looping through a dictionary:
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])