from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv("Flash Card Program/data/to_learn.csv")
except FileNotFoundError:
    print("File couldn't be found, starting from original file")
    data = pandas.read_csv("Flash Card Program/data/french_words.csv")

to_learn = data.to_dict(orient="records")
current_card = {}

def next_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=back_card)

def is_known():
    try:
        to_learn.remove(current_card)
        data = pandas.DataFrame(to_learn)
        data.to_csv("Flash Card Program/data/to_learn.csv", index=False)
    except ValueError:
        print("You have learnt all of the words!")
        quit()

    next_word()

# setting up:
window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="Flash Card Program/images/card_front.png")
back_card = PhotoImage(file="Flash Card Program/images/card_back.png")
card_background = canvas.create_image(405, 267, image=card_front)
word = canvas.create_text(405, 267, text="", font=("Ariel", 60, "bold"))
language = canvas.create_text(405, 157, text="French", font=("Ariel", 40, "italic"))
canvas.grid(row=0, column=0, columnspan=2)

# cross button:
cross_img = PhotoImage(file="Flash Card Program/images/wrong.png")
cross_button = Button(image=cross_img, bg=BACKGROUND_COLOR, command=next_word)
cross_button.grid(row=1, column=0)

# tick button:
tick_img = PhotoImage(file="Flash Card Program/images/right.png")
tick_button = Button(image=tick_img, bg=BACKGROUND_COLOR, command=is_known)
tick_button.grid(row=1, column=1)

next_word()

window.mainloop()
