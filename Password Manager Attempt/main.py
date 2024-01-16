# imports:
from tkinter import *
import string
import random

# constants:
FONT = ("Courier", 14, "bold")
BG = "light blue"

# lists of avaible characters:
numbers = list(string.digits)
special_characters = list(string.punctuation)
letters = list(string.ascii_lowercase) + list(string.ascii_uppercase)

# calling password function with the passed in variables:
def call_password():
    generate_password(chars=entry_characters.get(), nums=entry_nums.get(), specials=entry_specials.get())

# actually generating the randomised password:
def generate_password(chars, nums, specials):
    password = ""
    password_chars = int(chars)
    password_nums = int(nums)
    password_specs = int(specials)
    for _ in range(0, password_chars):
        password += random.choice(letters)
    for _ in range(0, password_nums):
        password += random.choice(numbers)
    for _ in range(0, password_specs):
        password += random.choice(special_characters)
    shuffled_password = "".join(random.sample(password, len(password)))
    generated_password_label.config(text=shuffled_password)

# creating the window:
window = Tk()
window.title("Password Manager")
window.config(padx=55, pady=50, bg=BG)

# characters:
num_of_characters = Label(text="Number of characters:", font=FONT, bg=BG)
entry_characters = Entry(font=FONT)
num_of_characters.grid(column=0, row=0)
entry_characters.grid(column=1, row=0, pady=5)

# specifics:
num_of_nums = Label(text="Number of numbers:", font=FONT, bg=BG)
entry_nums = Entry(font=FONT)
num_of_specials = Label(text="Number of special characters:", font=FONT, bg=BG)
entry_specials = Entry(font=FONT)
num_of_nums.grid(column=0, row=1)
entry_nums.grid(column=1, row=1, pady=5)
num_of_specials.grid(column=0, row=2)
entry_specials.grid(column=1, row=2, pady=5)

# generate box:
generate = Button(text="Generate", font=FONT, command=call_password)
generate.grid(column=0, row=3, columnspan=2, pady=20)

# generated password:
generated_password_label = Label(font=("Courier", 20, "bold"), bg="light blue")
generated_password_label.grid(column=0, row=4, columnspan=2, pady=20)


window.mainloop()