from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


def start_time():
    countdown(5 * 60)


def countdown(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60

    canvas.itemconfig(timer, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, countdown, count - 1)


window = Tk()
window.title('Tomato')
window.config(padx=100, pady=50, bg=PINK)

title_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50), bg=PINK)
title_label.grid(column=1, row=0)


canvas = Canvas(width=200, height=224, bg=PINK, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer = canvas.create_text(100, 130, text="00:00", fill="white",
                           font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


start_butt = Button(text='start', highlightthickness=0, command=start_time)
start_butt.grid(column=0, row=2)

reset_butt = Button(text='reset', highlightthickness=0)
reset_butt.grid(column=2, row=2)

check_marks = Label(text="✓", fg=GREEN, bg=PINK)
check_marks.grid(column=1, row=3)

window.mainloop()
