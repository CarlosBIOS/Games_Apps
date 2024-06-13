import tkinter as tk
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = '✔'
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset_time():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    timer_label.config(text='Timer')
    check_mark.config(text='')
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_time():
    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        timer_label.config(text='Break', fg=RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        check_mark['text'] += CHECK_MARK
        timer_label.config(text='Break', fg=PINK)
    else:
        count_down(WORK_MIN * 60)
        timer_label.config(text='Work', fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global timer
    count_min = math.floor(count / 60)  # arrendonda para baixo, ou seja, 3.9=3
    count_sec = count % 60  # é o resto entre count e 60, para dar os segundos
    if count_sec < 10:
        count_sec = f'0{count_sec}'

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        timer = window.after(1000, count_down, count - 1)  # é o cronómetro, 1000 milisegundos é 1 segundo!!
    else:
        start_time()
        mark = ''
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += CHECK_MARK
        check_mark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title('Pomodoro App')
window.config(padx=50, pady=50, bg=YELLOW)
window.minsize(width=450, height=450)
window.maxsize(width=450, height=450)


timer_label = tk.Label(text='Timer', bg=YELLOW, font=(FONT_NAME, 50), fg=GREEN)
timer_label.grid(row=0, column=1)

canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=False)
tomato_image = tk.PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_image)  # x=102(200/2) e y=112(224/2)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)

start = tk.Button(text='Start', font=(FONT_NAME, 15), command=start_time, highlightthickness=False)
reset = tk.Button(text='Reset', font=(FONT_NAME, 15), command=reset_time, highlightthickness=False)
start.grid(row=2, column=0)
reset.grid(row=2, column=2)

check_mark = tk.Label(bg=YELLOW, highlightthickness=False, fg=GREEN, font=(FONT_NAME, 12))
check_mark.grid(row=3, column=1)

window.mainloop()
