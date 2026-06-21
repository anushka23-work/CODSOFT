import tkinter as tk
from tkinter import messagebox
from task_manager import load_tasks, save_tasks

# Task load karein
tasks = load_tasks()

def refresh_list():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

def add_task(event=None):
    task = task_entry.get()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        refresh_list()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Enter a task first!")

def delete_task():
    try:
        selected = listbox.curselection()[0]
        tasks.pop(selected)
        save_tasks(tasks)
        refresh_list()
    except:
        messagebox.showwarning("Warning", "Select a task to delete.")

def update_task():
    try:
        selected = listbox.curselection()[0]
        new_task = task_entry.get()
        if new_task:
            tasks[selected] = new_task
            save_tasks(tasks)
            refresh_list()
            task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Enter new text to update.")
    except:
        messagebox.showwarning("Warning", "Select a task to update.")

# Main Window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x520")
root.configure(bg="#f8f9fa")

# Heading
tk.Label(root, text="✨ My To-Do List ✨", font=("Segoe UI", 20, "bold"), 
         bg="#f8f9fa", fg="#6f42c1").pack(pady=15)

# Entry Field
task_entry = tk.Entry(root, width=30, font=("Arial", 12), borderwidth=2, relief="groove")
task_entry.pack(pady=10)
task_entry.bind('<Return>', add_task) # Enter key support

# Buttons Frame
btn_frame = tk.Frame(root, bg="#f8f9fa")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Add", command=add_task, bg="#28a745", fg="white", 
          font=("Arial", 10, "bold"), width=8).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Update", command=update_task, bg="#ffc107", 
          font=("Arial", 10, "bold"), width=8).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Delete", command=delete_task, bg="#dc3545", fg="white", 
          font=("Arial", 10, "bold"), width=8).grid(row=0, column=2, padx=5)

# Listbox
listbox = tk.Listbox(root, width=45, height=12, font=("Arial", 11), 
                     selectbackground="#6f42c1", selectforeground="white", borderwidth=2)
listbox.pack(pady=15, padx=20)

refresh_list()
root.mainloop()