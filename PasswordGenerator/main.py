import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip # Run 'pip install pyperclip' in terminal if you want copy feature

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            messagebox.showerror("Error", "Length must be > 0")
            return
        
        chars = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(chars) for _ in range(length))
        
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
    except ValueError:
        messagebox.showerror("Error", "Enter a valid number!")

def copy_to_clipboard():
    password = password_entry.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Success", "Password copied to clipboard!")

# Main Window
root = tk.Tk()
root.title("Secure Password Generator")
root.geometry("400x350")
root.configure(bg="#2c3e50")

# Heading
tk.Label(root, text="🔐 Password Generator", font=("Segoe UI", 18, "bold"), 
         bg="#2c3e50", fg="#f1c40f").pack(pady=15)

# Input
tk.Label(root, text="Enter Length:", font=("Arial", 12), bg="#2c3e50", fg="white").pack()
length_entry = tk.Entry(root, font=("Arial", 12), width=10, justify="center")
length_entry.pack(pady=5)

# Buttons
btn_frame = tk.Frame(root, bg="#2c3e50")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Generate", command=generate_password, bg="#27ae60", 
          fg="white", font=("Arial", 10, "bold"), width=12).grid(row=0, column=0, padx=5)

tk.Button(btn_frame, text="Copy", command=copy_to_clipboard, bg="#3498db", 
          fg="white", font=("Arial", 10, "bold"), width=12).grid(row=0, column=1, padx=5)

# Result
password_entry = tk.Entry(root, font=("Segoe UI", 14), width=25, justify="center", bd=2)
password_entry.pack(pady=20)

root.mainloop()