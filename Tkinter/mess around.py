from tkinter import *

window = Tk()
window.minsize(490, 490)
window.config(padx=20, pady=20)

my_label = Label(text="I am a label!")
my_label.grid(row=0, column=0)

my_button1 = Button(text="Click me!")
my_button1.grid(row=1, column=1)

my_button2 = Button(text="Click me too!")
my_button2.grid(row=0, column=2)

my_entry = Entry()
my_entry.grid(row=2, column=3)

window.mainloop()
