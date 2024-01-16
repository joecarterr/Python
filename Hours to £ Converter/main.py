from tkinter import *

WAGE = 7.50
FONT = ("Arial", 12, "bold")

total_hours = float(0)
window = Tk()
window.title("Hours to £ Converter")
window.config(padx=20, pady=20)

def calculate():
    global total_hours
    user_input = float(num_to_add.get())
    total_hours += user_input
    num_to_add.delete(0, END)
    total.config(text=f"You have worked: {total_hours} hours")

def convert_time_to_money():
    hours_worked = entry.get()
    total_pay = float(hours_worked) * float(WAGE)
    money_output.config(text=f"£{total_pay}", font=FONT)

entry = Entry(width=7, font=FONT)
entry.focus()
entry.grid(row=0, column=1)

hours = Label(text="hours", font=FONT)
hours.grid(row=0, column=2)

equal_to = Label(text="is equal to", font=FONT)
equal_to.grid(row=1, column=0)

money_output = Label(text=f"£{0}", font=FONT)
money_output.grid(row=1, column=1)

convert = Button(text="Convert", command=convert_time_to_money, font=FONT)
convert.grid(row=2, column=1)

calc_hours = Label(text="Calculate hours worked:", font=FONT, padx=80)
calc_hours.grid(row=0, column=3)

num_to_add = Entry(font=FONT, width=7)
num_to_add.grid(row=1, column=3)

add_button = Button(text="Add", font=FONT, command=calculate)
add_button.grid(row=2, column=3)

total = Label(text="You have worked 0.0 hours", font=FONT)
total.grid(row=3, column=3)

window.mainloop()
