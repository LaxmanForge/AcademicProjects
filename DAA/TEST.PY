import tkinter as tk
from tkinter import simpledialog, messagebox
import time

# --------------------- Backend ---------------------
tasks = []  # list of tuples: (priority, task_name)

# -------- Bubble Sort (Easiest DAA Algorithm) --------
def bubble_sort(tasks):
    n = len(tasks)
    start = time.time()
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if tasks[j][0] > tasks[j + 1][0]:
                tasks[j], tasks[j + 1] = tasks[j + 1], tasks[j]
    end = time.time()
    elapsed = end - start
    return tasks, elapsed

# --------------------- GUI Functions ---------------------
def add_task():
    task_name = simpledialog.askstring("Task Name", "Enter task name:")
    if not task_name:
        return
    try:
        priority = int(simpledialog.askstring("Priority", "Enter task priority (1=High, 5=Low):"))
        if priority < 1 or priority > 5:
            raise ValueError
    except:
        messagebox.showerror("Invalid Priority", "Priority must be a number between 1 and 5")
        return
    
    tasks.append((priority, task_name))
    update_task_list()

def delete_task():
    selected = task_listbox.curselection()
    if not selected:
        return
    index = selected[0]
    tasks.pop(index)
    update_task_list()

def sort_tasks():
    global tasks
    if not tasks:
        messagebox.showinfo("No Tasks", "Add some tasks first!")
        return
    
    sorted_tasks, elapsed = bubble_sort(tasks.copy())
    algo_name = "Bubble Sort"
    complexity = "Time Complexity: O(n²), Space: O(1)"
    
    tasks = sorted_tasks
    update_task_list()
    messagebox.showinfo("Sorting Complete", 
        f"Algorithm: {algo_name}\n{complexity}\nExecution Time: {elapsed:.6f} seconds")

def update_task_list():
    task_listbox.delete(0, tk.END)
    for prio, name in tasks:
        display_name = f"[{prio}] {name}"
        task_listbox.insert(tk.END, display_name)
        # Color code by priority
        if prio == 1:
            task_listbox.itemconfig(tk.END, {'bg': '#ff4d4d', 'fg': 'white'})
        elif prio == 2:
            task_listbox.itemconfig(tk.END, {'bg': '#ffb84d', 'fg': 'black'})
        elif prio == 3:
            task_listbox.itemconfig(tk.END, {'bg': '#ffff99', 'fg': 'black'})
        elif prio == 4:
            task_listbox.itemconfig(tk.END, {'bg': '#b3ffb3', 'fg': 'black'})
        else:
            task_listbox.itemconfig(tk.END, {'bg': '#e6f2ff', 'fg': 'black'})

# --------------------- GUI Setup ---------------------
root = tk.Tk()
root.title("Task Manager using Bubble Sort (DAA Mini Project)")

# Make window full-screen and allow ESC to exit
root.attributes('-fullscreen', True)
def exit_fullscreen(event):
    root.attributes('-fullscreen', False)
root.bind("<Escape>", exit_fullscreen)

root.config(bg="#e6f2ff")

# --------------------- Title ---------------------
title_label = tk.Label(
    root,
    text="Task Manager - Bubble Sort (DAA Mini Project)",
    font=("Arial", 28, "bold"),
    bg="#e6f2ff",
    fg="navy"
)
title_label.pack(pady=30)

# --------------------- Buttons ---------------------
frame = tk.Frame(root, bg="#e6f2ff")
frame.pack(pady=20)

add_button = tk.Button(frame, text="Add Task", command=add_task, bg='lightgreen',
                       width=20, height=2, font=("Arial", 14, "bold"))
add_button.grid(row=0, column=0, padx=20)

delete_button = tk.Button(frame, text="Delete Task", command=delete_task, bg='lightcoral',
                          width=20, height=2, font=("Arial", 14, "bold"))
delete_button.grid(row=0, column=1, padx=20)

sort_button = tk.Button(root, text="Sort (Bubble Sort)", command=sort_tasks, bg='lightblue',
                        width=25, height=2, font=("Arial", 14, "bold"))
sort_button.pack(pady=20)
exit_button = tk.Button(root, text="Exit", command=root.destroy, bg='gray', fg='white',
                        width=15, height=2, font=("Arial", 12, "bold"))
exit_button.pack(pady=10)


# --------------------- Listbox ---------------------
task_listbox = tk.Listbox(root, width=90, height=20, font=("Consolas", 14), bd=3, relief="groove")
task_listbox.pack(pady=30)

# --------------------- Start Mainloop ---------------------
root.mainloop()
