import tkinter as tk
import random

# Initialize scores
user_score = 0
computer_score = 0

def play(user_choice):
    global user_score, computer_score
    options = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(options)

    result_text = f"You chose {user_choice}, Computer chose {computer_choice}.\n"

    if user_choice == computer_choice:
        result_text += "It's a tie!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Paper' and computer_choice == 'Rock') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper'):
        user_score += 1
        result_text += "You win!"
    else:
        computer_score += 1
        result_text += "You lose!"

    result_label.config(text=result_text)
    score_label.config(text=f"Your Score: {user_score} | Computer Score: {computer_score}")

# GUI setup
root = tk.Tk()
root.title("Rock Paper Scissors")

tk.Label(root, text="Choose your option:", font=("Arial", 14)).pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack()

tk.Button(button_frame, text="Rock", width=15, command=lambda: play('Rock')).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Paper", width=15, command=lambda: play('Paper')).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Scissors", width=15, command=lambda: play('Scissors')).grid(row=0, column=2, padx=5)

result_label = tk.Label(root, text="", font=("Arial", 12), pady=10)
result_label.pack()

score_label = tk.Label(root, text="Your Score: 0 | Computer Score: 0", font=("Arial", 12))
score_label.pack()

tk.Button(root, text="Reset Scores", command=lambda: reset_scores()).pack(pady=5)

def reset_scores():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    score_label.config(text="Your Score: 0 | Computer Score: 0")
    result_label.config(text="")

root.mainloop()
