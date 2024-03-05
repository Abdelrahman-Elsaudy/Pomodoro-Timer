# To test this code, I recommend deleting the *60 on line 33 to test the timer in seconds not in minutes.

from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

SESSIONS = [
    {"Work Session 1": 25},
    {"Short Break 1": 5},
    {"Work Session 2": 25},
    {"Short Break 2": 5},
    {"Work Session 3": 25},
    {"Long Break": 20}
]

index = 0
marks = ""      # Indication of the amount of working sessions done.
is_working = True


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    start.config(state="disabled")    # To avoid multiple presses on start button.
    global is_working
    is_working = True
    for session in SESSIONS[index]:
        timer.config(text=session)
        countdown(int(SESSIONS[index][session]) * 60)


def countdown(time):
    if is_working:

        # Converting total time into minutes and seconds.
        time_min = math.floor(time / 60)
        if time_min < 10:
            time_min = f"0{time_min}"       # So that it becomes 00:00.
        time_sec = time % 60
        if time_sec < 10:
            time_sec = f"0{time_sec}"

        # Countdown Mechanism.
        if time > -1:
            canvas.itemconfig(timer_text, text=f"{time_min}:{time_sec}")
            window.after(1000, countdown, time-1)

        # Shifting to the next session when the previous one ends.
        else:
            global index, marks
            if index < len(SESSIONS)-1:
                index += 1

                # Marking accomplishing a work session.
                if index % 2 != 0:
                    marks += "✔️"
                    check.config(text=marks)
                start_timer()                 # Starting the next session.


# ---------------------------- TIMER RESET ------------------------------- #

def reset_action():
    start.config(state="active")
    global is_working, index, marks
    is_working = False
    index = 0
    marks = ""
    canvas.itemconfig(timer_text, text="00:00")
    timer.config(text="Timer")
    check.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=100, pady=50, background=YELLOW, highlightthickness=0)
window.title("Pomodoro")

canvas = Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 117, text="00:00", fill="white", font=("FONT_NAME", 35, "bold"))
canvas.grid(column=1, row=1)

start = Button(text="start", width=7, bg=YELLOW, highlightthickness=0, command=start_timer)
start.grid(column=0, row=2)

timer = Label(text="Timer", font=("FONT_NAME", 30, "bold"), fg="GREEN", bg=YELLOW)
timer.grid(column=1, row=0)

reset = Button(text="reset", width=7, bg=YELLOW, highlightthickness=0, command=reset_action)
reset.grid(column=2, row=2)

check = Label(fg=GREEN, bg=YELLOW, font=("FONT_NAME", 14, "bold"))
check.grid(column=1, row=3)

window.mainloop()
