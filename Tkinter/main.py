from tkinter import *

window = Tk()
window.title("Joes GUI Program")
window.minsize(width=600, height=600)

# Label:
my_label = Label(text="Hello", font=("Arial", 24, "bold"))
my_label.pack(side="bottom")

my_label["text"] = "hello" # altering the current text

# Entry:

def new_text():
    word_in_box = input.get()
    print(word_in_box)
    my_label.config(text=word_in_box)

input = Entry()
input.focus()
input.pack()

# Button:

total = 0
def on_click():
    global total
    total += 1
    my_label.config(text=total)

my_button = Button(text="Click Me", font=("Arial", 24, "bold"), command=new_text)
my_button.pack(side="left")


window.mainloop()
