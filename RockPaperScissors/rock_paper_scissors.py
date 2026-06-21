import tkinter as tk
from tkinter import messagebox
import random

class RPSGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.root.geometry("400x450")
        self.root.configure(bg="#f0f0f0")

        self.user_score = 0
        self.comp_score = 0

        # UI Heading
        tk.Label(root, text="Rock Paper Scissors", font=("Arial", 18, "bold"), bg="#f0f0f0").pack(pady=15)

        # Result Display
        self.result_label = tk.Label(root, text="Choose your move!", font=("Arial", 12), bg="#ffffff", width=40, height=4, relief="solid")
        self.result_label.pack(pady=10)

        # Game Buttons
        frame = tk.Frame(root, bg="#f0f0f0")
        frame.pack(pady=20)

        tk.Button(frame, text="Rock", width=10, bg="#add8e6", command=lambda: self.play("Rock")).grid(row=0, column=0, padx=5)
        tk.Button(frame, text="Paper", width=10, bg="#add8e6", command=lambda: self.play("Paper")).grid(row=0, column=1, padx=5)
        tk.Button(frame, text="Scissors", width=10, bg="#add8e6", command=lambda: self.play("Scissors")).grid(row=0, column=2, padx=5)

        # Score Tracking
        self.score_label = tk.Label(root, text="User: 0 | Computer: 0", font=("Arial", 12, "bold"), bg="#f0f0f0")
        self.score_label.pack(pady=10)

        # Reset Button
        tk.Button(root, text="Reset Score", command=self.reset_game).pack(pady=5)

    def play(self, user_choice):
        comp_choice = random.choice(["Rock", "Paper", "Scissors"])
        
        if user_choice == comp_choice:
            result = "It's a Tie!"
            bg_color = "#fff3cd" # Yellow
        elif (user_choice == "Rock" and comp_choice == "Scissors") or \
             (user_choice == "Paper" and comp_choice == "Rock") or \
             (user_choice == "Scissors" and comp_choice == "Paper"):
            result = "You Win!"
            self.user_score += 1
            bg_color = "#d4edda" # Green
        else:
            result = "You Lose!"
            self.comp_score += 1
            bg_color = "#f8d7da" # Red

        self.result_label.config(text=f"You: {user_choice} | Computer: {comp_choice}\n{result}", bg=bg_color)
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