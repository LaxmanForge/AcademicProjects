print("ChronoDesk is starting...")

import tkinter as tk
from time import strftime, time

# ---------------- Main Window ----------------
root = tk.Tk()
root.title("ChronoDesk")
root.configure(bg="#1E1E2F")  # Modern dark background
root.geometry("800x600")  # Initial size, adjustable

# ---------------- Fonts and Colors ----------------
FONT_LARGE = ("Poppins", 80, "bold")
FONT_MEDIUM = ("Poppins", 28)
ACCENT_COLOR = "#62FAA4"   # Modern coral
TEXT_COLOR = "#000000"     # Soft white
BG_COLOR = "#0F4637"       # Main background
FRAME_COLOR = "#033A2E"    # Slightly lighter for frames
BUTTON_COLOR = "#65F4B4"   # Button background

# ---------------- Navigation ----------------
def show_frame(frame):
    frame.tkraise()

nav_frame = tk.Frame(root, bg=FRAME_COLOR)
nav_frame.pack(side="top", fill="x", pady=10)

clock_btn = tk.Button(nav_frame, text="Clock", fg=TEXT_COLOR, bg=BUTTON_COLOR, bd=0,
                      font=FONT_MEDIUM, activebackground=ACCENT_COLOR,
                      activeforeground=BG_COLOR, command=lambda: show_frame(clock_frame))
stopwatch_btn = tk.Button(nav_frame, text="Stopwatch", fg=TEXT_COLOR, bg=BUTTON_COLOR, bd=0,
                          font=FONT_MEDIUM, activebackground=ACCENT_COLOR,
                          activeforeground=BG_COLOR, command=lambda: show_frame(stopwatch_frame))
about_btn = tk.Button(nav_frame, text="About", fg=TEXT_COLOR, bg=BUTTON_COLOR, bd=0,
                      font=FONT_MEDIUM, activebackground=ACCENT_COLOR,
                      activeforeground=BG_COLOR, command=lambda: show_frame(about_frame))

clock_btn.pack(side="left", padx=50)
stopwatch_btn.pack(side="left", padx=50)
about_btn.pack(side="left", padx=50)

# ---------------- Frames ----------------
container = tk.Frame(root, bg=BG_COLOR)
container.pack(fill="both", expand=True)

clock_frame = tk.Frame(container, bg=BG_COLOR)
stopwatch_frame = tk.Frame(container, bg=BG_COLOR)
about_frame = tk.Frame(container, bg=BG_COLOR)

for frame in (clock_frame, stopwatch_frame, about_frame):
    frame.place(relx=0, rely=0, relwidth=1, relheight=1)

# ---------------- Clock ----------------
time_label = tk.Label(clock_frame, font=FONT_LARGE, fg=ACCENT_COLOR, bg=BG_COLOR)
time_label.pack(expand=True)
date_label = tk.Label(clock_frame, font=FONT_MEDIUM, fg=TEXT_COLOR, bg=BG_COLOR)
date_label.pack()

def update_clock():
    time_label.config(text=strftime("%H:%M:%S"))
    date_label.config(text=strftime("%A, %d %B %Y"))
    time_label.after(1000, update_clock)

# ---------------- Stopwatch ----------------
sw_time = tk.StringVar(value="00:00:00")
sw_label = tk.Label(stopwatch_frame, textvariable=sw_time, font=FONT_LARGE, fg=ACCENT_COLOR, bg=BG_COLOR)
sw_label.pack(expand=True)

sw_running = False
sw_counter = 0

def update_stopwatch():
    global sw_counter
    if sw_running:
        sw_counter += 1
        hours = sw_counter // 3600
        minutes = (sw_counter % 3600) // 60
        seconds = sw_counter % 60
        sw_time.set(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
        sw_label.after(1000, update_stopwatch)

def sw_start():
    global sw_running
    sw_running = True
    update_stopwatch()

def sw_pause():
    global sw_running
    sw_running = False

def sw_reset():
    global sw_running, sw_counter
    sw_running = False
    sw_counter = 0
    sw_time.set("00:00:00")

sw_buttons = tk.Frame(stopwatch_frame, bg=BG_COLOR)
sw_buttons.pack(pady=40)

tk.Button(sw_buttons, text="Start", fg=TEXT_COLOR, bg=ACCENT_COLOR, font=FONT_MEDIUM, bd=0, width=12, command=sw_start).pack(side="left", padx=10)
tk.Button(sw_buttons, text="Pause", fg=TEXT_COLOR, bg=ACCENT_COLOR, font=FONT_MEDIUM, bd=0, width=12, command=sw_pause).pack(side="left", padx=10)
tk.Button(sw_buttons, text="Reset", fg=TEXT_COLOR, bg=ACCENT_COLOR, font=FONT_MEDIUM, bd=0, width=12, command=sw_reset).pack(side="left", padx=10)

# ---------------- About ----------------
about_label = tk.Label(about_frame, text="ChronoDesk\nVersion 1.0\nDeveloped by Laxman Singh", 
                       font=FONT_MEDIUM, fg=TEXT_COLOR, bg=BG_COLOR, justify="center")
about_label.pack(expand=True)

# ---------------- Start App ----------------
update_clock()
show_frame(clock_frame)
root.mainloop()

#Second One
'''
import tkinter as tk
import time

root = tk.Tk()
root.title("ChronoDesk - Simple Clock & Stopwatch")
root.geometry("500x300")
root.config(bg="#101010")

# Colors and fonts
ACCENT = "#00FF88"
TEXT = "#FFFFFF"
FONT_LARGE = ("Poppins", 36, "bold")
FONT_MED = ("Poppins", 14)

# ---------------- CLOCK ----------------
clock_label = tk.Label(root, text="", font=FONT_LARGE, fg=ACCENT, bg="#101010")
clock_label.pack(pady=20)

def update_clock():
    current_time = time.strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    root.after(1000, update_clock)  # update every second

# ---------------- STOPWATCH ----------------
stopwatch_label = tk.Label(root, text="00:00:00", font=FONT_LARGE, fg=TEXT, bg="#101010")
stopwatch_label.pack(pady=10)

running = False
elapsed = 0
start_time = 0

def start_stopwatch():
    global running, start_time
    if not running:
        running = True
        start_time = time.time() - elapsed
        update_stopwatch()

def stop_stopwatch():
    global running, elapsed
    running = False
    elapsed = time.time() - start_time

def reset_stopwatch():
    global elapsed
    elapsed = 0
    stopwatch_label.config(text="00:00:00")

def update_stopwatch():
    if running:
        global elapsed
        elapsed = time.time() - start_time
        mins, secs = divmod(int(elapsed), 60)
        hours, mins = divmod(mins, 60)
        stopwatch_label.config(text=f"{hours:02}:{mins:02}:{secs:02}")
        root.after(1000, update_stopwatch)

# ---------------- BUTTONS ----------------
button_frame = tk.Frame(root, bg="#101010")
button_frame.pack(pady=10)

tk.Button(button_frame, text="Start", font=FONT_MED, bg=ACCENT, fg="#000", width=8, command=start_stopwatch).pack(side="left", padx=10)
tk.Button(button_frame, text="Stop", font=FONT_MED, bg=ACCENT, fg="#000", width=8, command=stop_stopwatch).pack(side="left", padx=10)
tk.Button(button_frame, text="Reset", font=FONT_MED, bg=ACCENT, fg="#000", width=8, command=reset_stopwatch).pack(side="left", padx=10)

# ---------------- START APP ----------------
update_clock()
root.mainloop()
'''