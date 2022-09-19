def greet_with(user_name, user_location):
    print(f"Hello {user_name}")
    print(f"Wow {user_location} is a nice place")


name = input("What's your name?:\n")
location = input("Where do you live?:\n")
# whatever is first is assigned to the first parameter (argument(name is assigned to user_name)) and then in order after
# that e.g. (location will be = to user location)
greet_with(name, location)

