from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer_duration = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer_duration)
    canvas.itemconfig(count_text, text="00:00")
    timer.config(text="Timer", fg=GREEN)
    tick.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        timer.config(text="Break", fg=RED)
        count_down(int(LONG_BREAK_MIN * 60))
    elif reps % 2 == 0:
        timer.config(text="Break", fg=PINK)
        count_down(int(SHORT_BREAK_MIN * 60))
    else:
        timer.config(text="Work", fg=GREEN)
        count_down(int(WORK_MIN * 60))

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(count_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer_duration
        timer_duration = window.after(1000, count_down, count-1)
    else:
        start_timer()
        check_marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            check_marks += "✔"
        tick.config(text=check_marks)
        


# ---------------------------- UI SETUP ------------------------------- #

# creating window:
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

# tomato image and timer:
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="Pomodoro Timer/tomato.png")
canvas.create_image(100, 112, image=tomato_image)
count_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(column=1, row=1)

# timer text:
timer = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40, "bold"))
timer.grid(column=1, row=0)

# start button:
start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

# reset button:
reset_button = Button(text="Restart", command=reset_timer)
reset_button.grid(column=2, row= 2)

# ticks:
tick = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 12, "bold"))
tick.grid(column=1, row=3)

# keeping the window open:
window.mainloop()
