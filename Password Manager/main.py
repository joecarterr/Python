from tkinter import *
from tkinter import messagebox
import string
import random
import math
import pyperclip
import json

EMAIL = "joecarterx07@gmail.com"

nr_characters = random.randint(4, 12) # *3 in real password

def find_password():
    website = website_entry.get()
    try:
        with open("Password Manager\data.json", "r") as data:
            loaded = json.load(data)
            email = loaded[website]["email"]
            password = loaded[website]["password"]
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found.")
    except KeyError:
        messagebox.showinfo(title="Error", message=f"No details for {website} exist.")
    else:
        messagebox.showinfo(title=website, message=f"Email: {email}\nPasword: {password}")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# generation of randomised password
def generating_user_password():
    password = ""
    # lists of avaible characters:
    numbers = list(string.digits)
    special_characters = list(string.punctuation)
    letters = list(string.ascii_lowercase) + list(string.ascii_uppercase)

    for _ in range(math.ceil(nr_characters)):
        random_nums = random.choice(numbers)
        random_spec_chars = random.choice(special_characters)
        random_letters = random.choice(letters)
        password += random_nums
        password += random_spec_chars
        password += random_letters

    shuffled_password = "".join(random.sample(password, len(password)))
    password_entry.insert(0, shuffled_password)
    pyperclip.copy(password_entry.get())
    

# ---------------------------- SAVE PASSWORD ------------------------------- #
# adding the users website:
def add_website():

    website_data = website_entry.get()
    email_data = email_entry.get()
    password_data = password_entry.get()
    new_data = {
        website_data: {
        "email": email_data,
        "password": password_data,
        }
    }

    if len(website_data) == 0 or len(email_data) == 0 or len(password_data) == 0:
        messagebox.showerror(title="Error:", message="You have left some of your fields blank, please go back and fill them in.")
    else:
        try:
            with open("Password Manager/data.json", "r") as data_file:
                # reading old data:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("Password Manager/data.json", "w") as data_file:
                # saving updated data:
                json.dump(new_data, data_file, indent=4)
        else:
            # updating old data with new data:
            data.update(new_data)

            with open("Password Manager/data.json", "w") as data_file:
                # saving updated data:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
        


# ---------------------------- UI SETUP ------------------------------- #
# creating window:
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# creating lock image:
lock_image = PhotoImage(file="Password Manager/logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

# website:
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
website_entry = Entry(width=50)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)

# email/username:
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
email_entry = Entry(width=50)
email_entry.insert(0, EMAIL)
email_entry.grid(row=2, column=1, columnspan=2)

# password:
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
password_entry = Entry(width=50)
password_entry.grid(row=3, column=1, columnspan=2)

# generation of password:
generate_password = Button(text="Generate Password", command=generating_user_password)
generate_password.grid(row=3, column=2)

# add the password:
add_password = Button(text="Add", width=42, command=add_website)
add_password.grid(row=4, column=1, columnspan=2)

# search password:
search_password = Button(text="Search", width=14, command=find_password)
search_password.grid(row=1, column=2)

# constant loop:
window.mainloop()
