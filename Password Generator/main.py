# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Hard Level - Order of characters randomised:
password_list = []
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
for letter in range(0, nr_letters + 1):
    letter_selection = (random.choice(letters))
    password_list.append(letter_selection)
    # print(letter_selection, end="")
    # "".join(letter_selection)
for symbol in range(0, nr_symbols + 1):
    symbol_selection = (random.choice(symbols))
    password_list.append(symbol_selection)
    # print(symbol_selection, end="")
for number in range(0, nr_numbers + 1):
    number_selection = (random.choice(numbers))
    password_list.append(number_selection)
    # print(number_selection, end="")
random.shuffle(password_list)

password = ""
for character in password_list:
    password += character

print(f"Your password is {password}")
