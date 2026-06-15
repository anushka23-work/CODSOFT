import tkinter as tk
from tkinter import messagebox
from generator import generate_password


def create_password():
    try:
        length = int(length_entry.get())

        if length <= 0:
            messagebox.showerror("Error", "Length must be greater than 0")
            return

        password = generate_password(length)

        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)

    except ValueError:
        messagebox.showerror("Error", "Enter a valid number")


root = tk.Tk()
root.title("Password Generator")
root.geometry("400x250")

tk.Label(
    root,
    text="Password Generator",
    font=("Arial", 18, "bold")
).pack(pady=10)

tk.Label(
    root,
    text="Enter Password Length:"
).pack()

length_entry = tk.Entry(root)
length_entry.pack(pady=5)

tk.Button(
    root,
    text="Generate Password",
    command=create_password
).pack(pady=10)

password_entry = tk.Entry(root, width=35)
password_entry.pack(pady=10)

root.mainloop()