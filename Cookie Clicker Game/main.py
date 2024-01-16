from tkinter import *

# constants:
DARK_BLUE = "#191D88"
LIGHT_BLUE = "#337CCF"
YELLOW = "#FFC436"
FONT_NAME = "Courier"
num_of_cookies = 0
cookie_amount = 1

# upgrade your cookie:
def upgrade_cookie():
    global cookie_amount
    cookie_amount *= 2

# cookie is clicked:
def on_click(event):
    global num_of_cookies
    global cookie_amount
    num_of_cookies += cookie_amount
    cookie_number.config(text=f"{num_of_cookies} Cookies")

# setting up window:
window = Tk()
window.config(padx=100, pady=60, bg=LIGHT_BLUE)
window.title("Cookie Clicker")

# cookie image:
canvas = Canvas(width=250, height=250, bg=LIGHT_BLUE, highlightthickness=0)
cookie_img = PhotoImage(file="Cookie Clicker Game/cookie_clicker.png")
canvas.create_image(125, 125, image=cookie_img)
canvas.bind("<Button-1>", on_click)
canvas.grid(row=2, column=1)

# number of cookies:
cookie_number = Label(text="0 Cookies", fg=YELLOW, bg=LIGHT_BLUE, font=(FONT_NAME, 20, "bold"), pady=20)
cookie_number.grid(row=1, column=1)

# upgrade cookie:
upgrade = Button(text="Upgrade", command=upgrade_cookie, font=(FONT_NAME, 12, "bold"), bg=DARK_BLUE, fg="white")
upgrade.grid(column=1, row=3)

# users bakery name:
name_of_bakery = input("What's your name?: ")
name_label = Label(text=f"{name_of_bakery}'s Bakery", font=(FONT_NAME, 20, "bold"), fg=YELLOW, bg=LIGHT_BLUE)
name_label.grid(row=0, column=1)

# keeping the window open:
window.mainloop()
