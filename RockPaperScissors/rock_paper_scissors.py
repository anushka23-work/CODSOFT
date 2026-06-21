import tkinter as tk
from tkinter import messagebox
import random

class RPSGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors Pro")
        self.root.geometry("450x500")
        self.root.configure(bg="#f0f2f5")

        self.user_score = 0
        self.comp_score = 0

        # Title
        tk.Label(root, text="Rock Paper Scissors", font=("Segoe UI", 22, "bold"), bg="#f0f2f5", fg="#333").pack(pady=20)

        # Result Display Area
        self.result_label = tk.Label(root, text="Select your move to start!", font=("Segoe UI", 13), 
                                     bg="#ffffff", width=45, height=5, relief="flat", highlightbackground="#ddd", highlightthickness=1)
        self.result_label.pack(pady=10)

        # Button Frame
        frame = tk.Frame(root, bg="#f0f2f5")
        frame.pack(pady=20)

        # Buttons with Hover Effects
        self.create_button(frame, "Rock", 0, 0, "#87CEFA")
        self.create_button(frame, "Paper", 0, 1, "#98FB98")
        self.create_button(frame, "Scissors", 0, 2, "#FFB6C1")

        # Score Display
        self.score_label = tk.Label(root, text="User: 0 | Computer: 0", font=("Segoe UI", 14, "bold"), bg="#f0f2f5")
        self.score_label.pack(pady=10)

        # Reset Button
        tk.Button(root, text="Reset Game", command=self.reset_game, font=("Segoe UI", 10), bg="#ff6b6b", fg="white").pack(pady=10)

    def create_button(self, frame, text, row, col, color):
        btn = tk.Button(frame, text=text, width=10, height=2, bg=color, font=("Segoe UI", 10, "bold"),
                        command=lambda: self.play(text))
        btn.grid(row=row, column=col, padx=10)
        # Add hover effects
        btn.bind("<Enter>", lambda e: e.widget.config(relief="sunken"))
        btn.bind("<Leave>", lambda e: e.widget.config(relief="raised"))

    def play(self, user_choice):
        comp_choice = random.choice(["Rock", "Paper", "Scissors"])
        
        if user_choice == comp_choice:
            result = "It's a Tie!"
            bg_color = "#fff3cd"
        elif (user_choice == "Rock" and comp_choice == "Scissors") or \
             (user_choice == "Paper" and comp_choice == "Rock") or \
             (user_choice == "Scissors" and comp_choice == "Paper"):
            result = "You Win!"
            self.user_score += 1
            bg_color = "#d4edda"
        else:
            result = "You Lose!"
            self.comp_score += 1
            bg_color = "#f8d7da"

        self.result_label.config(text=f"You: {user_choice}  |  Comp: {comp_choice}\n{result}", bg=bg_color)
        self.score_label.config(text=f"User: {self.user_score} | Computer: {self.comp_score}")

    def reset_game(self):
        self.user_score = 0
        self.comp_score = 0
        self.score_label.config(text="User: 0 | Computer: 0")
        self.result_label.config(text="Game Reset! Choose your move.", bg="#ffffff")

if __name__ == "__main__":
    root = tk.Tk()
    game = RPSGame(root)
    root.mainloop()