import tkinter as tk
from tkinter import messagebox
from task_manager import load_tasks, save_tasks

tasks = load_tasks()


def refresh_list():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)


def add_task():
    task = task_entry.get()

    if task:
        tasks.append(task)
        save_tasks(tasks)
        refresh_list()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Enter a task")


def delete_task():
    try:
        selected = listbox.curselection()[0]
        tasks.pop(selected)
        save_tasks(tasks)
        refresh_list()
    except:
        messagebox.showwarning("Warning", "Select a task")


root = tk.Tk()
root.title("To-Do List")
root.geometry("400x450")

heading = tk.Label(
    root,
    text="To-Do List",
    font=("Arial", 18, "bold")
)
heading.pack(pady=10)

task_entry = tk.Entry(root, width=35)
task_entry.pack(pady=10)

tk.Button(
    root,
    text="Add Task",
    command=add_task
).pack(pady=5)

listbox = tk.Listbox(root, width=40, height=12)
listbox.pack(pady=10)

tk.Button(
    root,
    text="Delete Task",
    command=delete_task
).pack(pady=5)

refresh_list()

root.mainloop()
