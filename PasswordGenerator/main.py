import tkinter as tk
from tkinter import messagebox
import random
import string


def generate_password():

    try:
        length = int(length_entry.get())

        if length <= 0:
            messagebox.showerror("Error", "Length must be greater than 0")
            return


        

        characters = string.ascii_letters + string.digits + string.punctuation

        password = ''.join(random.choice(characters) for _ in range(length))


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
    command=generate_password
).pack(pady=10)

password_entry = tk.Entry(root, width=35)
password_entry.pack(pady=10)

root.mainloop()
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x250")
root.resizable(False, False)

# Heading
heading = tk.Label(
    root,
    text="Password Generator",
    font=("Arial", 18, "bold")
)
heading.pack(pady=10)

# Length Input
tk.Label(root, text="Enter Password Length:", font=("Arial", 12)).pack()

length_entry = tk.Entry(root, font=("Arial", 12))
length_entry.pack(pady=5)

# Generate Button
generate_btn = tk.Button(
    root,
    text="Generate Password",
    font=("Arial", 12),
    command=generate_password
)
generate_btn.pack(pady=10)

# Password Output
password_entry = tk.Entry(
    root,
    font=("Arial", 12),
    width=30,
    justify="center"
)
password_entry.pack(pady=10)

root.mainloop()

