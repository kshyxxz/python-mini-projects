import tkinter as tk

WORK_TIME = 25 * 60
SHORT_BREAK = 5 * 60
LONG_BREAK = 15 * 60

session_count = 0
timer_running = False
after_id = None

def countdown(seconds):
    global timer_running, after_id
    mins, secs = divmod(seconds, 60)
    timer_label.config(text=f"{mins:02d}:{secs:02d}")
    if seconds > 0:
        after_id = window.after(1000, countdown, seconds - 1)
    else:
        window.bell() 
        timer_running = False
        start_timer()  

def start_timer():
    global session_count, timer_running
    if timer_running:
        return
    timer_running = True
    if session_count % 8 == 7:
        status_label.config(text="Long Break", fg="blue")
        countdown(LONG_BREAK)
    elif session_count % 2 == 0:
        status_label.config(text="Work", fg="green")
        countdown(WORK_TIME)
    else:
        status_label.config(text="Short Break", fg="orange")
        countdown(SHORT_BREAK)
    session_count += 1


def reset_timer():
    global session_count, timer_running, after_id
    timer_running = False
    session_count = 0
    if after_id is not None:
        window.after_cancel(after_id)
        after_id = None
    timer_label.config(text="25:00")
    status_label.config(text="Ready", fg="black")


window = tk.Tk()
window.title("Pomodoro Timer")
window.geometry("350x250")
window.resizable(False, False)

title_label = tk.Label(window,text="Pomodoro Timer",font=("Arial", 18, "bold"))
title_label.pack(pady=10)

timer_label = tk.Label(window,text="25:00",font=("Arial", 48, "bold"))
timer_label.pack(pady=10)

status_label = tk.Label(window,text="Ready",font=("Arial", 18))
status_label.pack()

button_frame = tk.Frame(window)
button_frame.pack(pady=20)

start_button = tk.Button(button_frame,text="Start",width=10,font=("Arial", 12),command=start_timer)
start_button.pack(side="left", padx=10)

reset_button = tk.Button(button_frame,text="Reset",width=10,font=("Arial", 12),command=reset_timer)
reset_button.pack(side="left", padx=10)

window.mainloop()