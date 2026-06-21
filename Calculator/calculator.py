import tkinter as tk

def click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Main Window
root = tk.Tk()
root.title("SMART CALCULATOR")
root.geometry("320x450")
root.resizable(False, False)

# Display
entry = tk.Entry(root, font=("Arial", 20), justify="right", bd=10)
entry.grid(row=0, column=0, columnspan=4, pady=10)

# Buttons Layout
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row = 1
col = 0

for button in buttons:
    if button == '=':
        cmd = calculate
    else:
        cmd = lambda b=button: click(b)

    tk.Button(
        root,
        text=button,

        width=5,
        height=2,
        font=("Arial", 14),
        command=cmd
    ).grid(row=row, column=col, padx=5, pady=5)

    col += 1
    if col > 3:
        col = 0
        row += 1

# Clear Button
tk.Button(
    root,
    text="CLEAR",
    width=28,
    height=2,
    font=("Arial", 12),
    command=clear
).grid(row=row+1, column=0, columnspan=4, pady=10)
root.mainloop()


