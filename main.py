from tkinter import *
import math

# ---------------------------- CONSTANTS AND VARIABLES ------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
repeat = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def timer_reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title.config(text="Timer")
    check_mark.config(text="")
    global repeat
    repeat = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global repeat
    repeat += 1
    focus = WORK_MIN * 60
    s_break = SHORT_BREAK_MIN * 60
    l_break = LONG_BREAK_MIN * 60

    if repeat % 8 == 0:
        timer_count(l_break)
        title.config(text="Long Break", fg=RED)
    elif repeat % 2 == 0:
        title.config(text="Break", fg=PINK)
        timer_count(s_break)
    else:
        title.config(text="Focus", fg=GREEN)
        timer_count(focus)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def timer_count(count):
    minutes = math.floor(count / 60)
    seconds = count % 60

    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, timer_count, count - 1)
    elif count == 0:
        start_timer()
        checkmarks = ""
        focus_sessions = math.floor(repeat / 2)
        for _ in range(focus_sessions):
            checkmarks += "✓"
            check_mark.config(text=checkmarks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(pady=50, padx=100, bg=YELLOW)

title = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 55), bg=YELLOW)
title.grid(column=1, row=0)
check_mark = Label(fg=GREEN, font=(FONT_NAME, 30, "bold"), bg=YELLOW)
check_mark.grid(column=1, row=3)

canvas = Canvas(width=200 , height=234, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start = Button(text="Start", fg=PINK, highlightthickness=0, bg=YELLOW, font=FONT_NAME, relief="groove",
               command=start_timer)
start.grid(column=0, row=2)
reset = Button(text="Reset", fg=PINK, highlightthickness=0, bg=YELLOW, font=FONT_NAME, relief="groove",
               command=timer_reset)
reset.grid(column=2, row=2)

window.mainloop()
