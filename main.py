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
REPS = 0
TIMER = None


def reset_timer():
    window.after_cancel(TIMER)
    canvas.itemconfig(timer, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    global REPS
    REPS = 0
    start_butt.config(state="normal")


def start_time():
    start_butt.config(state="disabled")
    global REPS
    REPS += 1

    work_min = WORK_MIN * 60
    short_break_min = SHORT_BREAK_MIN * 60
    long_break_min = LONG_BREAK_MIN * 60

    if REPS % 8 == 0:
        countdown(long_break_min)
        title_label.config(text="Break", fg=RED)
    elif REPS % 2 == 0:
        countdown(short_break_min)
        title_label.config(text="Break", fg=YELLOW)
    else:
        countdown(work_min)
        title_label.config(text="Work", fg=GREEN)


def countdown(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'

    canvas.itemconfig(timer, text=f"{count_min}:{count_sec}")
    if count > 0:
        global TIMER
        TIMER = window.after(1000, countdown, count - 1)
    else:
        start_time()
        marks = ""
        for _ in range(math.floor(REPS/2)):
            marks += "✓"
        check_marks.config(text=marks)


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

reset_butt = Button(text='reset', highlightthickness=0, command=reset_timer)
reset_butt.grid(column=2, row=2)

check_marks = Label(text="", fg=GREEN, bg=PINK, font=(FONT_NAME, 20))
check_marks.grid(column=1, row=3)

window.mainloop()
