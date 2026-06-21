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

# Display (Colourful)
entry = tk.Entry(root, font=("Arial", 20), justify="right", bd=10, bg="#f0f8ff")
entry.grid(row=0, column=0, columnspan=4, pady=10)

# Buttons Layout (Colourful)
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row = 1
col = 0

# Button Colors
colors = {'/': '#ff7f50', '*': '#ff7f50', '-': '#ff7f50', '+': '#ff7f50', '=': '#90ee90'}

for button in buttons:
    if button == '=':
        cmd = calculate
        btn_color = colors.get(button, '#d3d3d3')
    elif button in colors:
        cmd = lambda b=button: click(b)
        btn_color = colors.get(button, '#d3d3d3')
    else:
        cmd = lambda b=button: click(b)
        btn_color = '#add8e6' # Light Blue for numbers

    tk.Button(
        root, text=button, width=5, height=2, font=("Arial", 14, "bold"),
        command=cmd, bg=btn_color
    ).grid(row=row, column=col, padx=5, pady=5)

    col += 1
    if col > 3:
        col = 0
        row += 1

# Clear Button (Colourful)
tk.Button(
    root, text="CLEAR", width=28, height=2, font=("Arial", 12, "bold"),
    command=clear, bg="#ffcccb"
).grid(row=row+1, column=0, columnspan=4, pady=10)

root.mainloop()