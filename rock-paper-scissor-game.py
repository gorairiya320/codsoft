import tkinter as tk
from tkinter import messagebox
import random

# Function for determine the winner
def determine_winner(user_choice, comp_choice):
    if user_choice == comp_choice:
        return " Oops,It's a tie!"
    elif (user_choice == "Rock" and comp_choice == "Scissors") or \
         (user_choice == "Scissors" and comp_choice == "Paper") or \
         (user_choice == "Paper" and comp_choice == "Rock"):
        return "You win the game!"
    else:
        return "You lose the game!"

# Function for handle user choice
def user_choice(choice):
    global rounds_played
    if rounds_played < 5:
        comp_choice = random.choice(["Rock", "Paper", "Scissors"])
        result = determine_winner(choice, comp_choice)
        messagebox.showinfo("Result", f"Your choice: {choice}\nComputer's choice: {comp_choice}\n{result}")
        update_score(result)
        rounds_played += 1
        if rounds_played == 5:
            determine_final_winner()
    else:
        determine_final_winner()

# For update score
def update_score(result):
    global user_score, comp_score
    if "win" in result:
        user_score += 1
    elif "lose" in result:
        comp_score += 1
    score_label.config(text=f"User: {user_score}  Computer: {comp_score}")

# Function to determine the final winner
def determine_final_winner():
    if user_score > comp_score:
        final_result = "Congratulations! You are the overall winner!"
    elif user_score < comp_score:
        final_result = "Sorry! The computer is the overall winner!"
    else:
        final_result = "It's an overall tie!"
    messagebox.showinfo("Final Result", final_result)
    ask_play_again()

# Function to ask if user wants to play again
def ask_play_again():
    if messagebox.askyesno("Play Again", "Do you want to play again?"):
        reset_game()
    else:
        root.quit()

# Function to reset the game
def reset_game():
    global user_score, comp_score, rounds_played
    user_score = 0
    comp_score = 0
    rounds_played = 0
    score_label.config(text=f"User: {user_score}  Computer: {comp_score}")

# Setting the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("480x380")

#  for Score tracking
user_score = 0
comp_score = 0
rounds_played = 0

# Creating widgets
welcome_label = tk.Label(root, text="Choose Rock, Paper, or Scissors", font=("verdana", 14))

rock_button = tk.Button(root, text="Rock", command=lambda: user_choice("Rock"), bg='blue', fg='white', font=("verdana", 10))
paper_button = tk.Button(root, text="Paper", command=lambda: user_choice("Paper"), bg='blue', fg='white', font=("verdana", 10))
scissors_button = tk.Button(root, text="Scissors", command=lambda: user_choice("Scissors"), bg='blue', fg='white', font=("verdana", 10))
text_Label=tk.Label(root,text='🎉Winner is declared after 5 round🎉', font=("verdana", 14))
score_label = tk.Label(root, text=f"User: {user_score}  Computer: {comp_score}", font=("verdana", 14))

# all widgets
welcome_label.pack(pady=20)
rock_button.pack(pady=5)
paper_button.pack(pady=5)
scissors_button.pack(pady=5)
text_Label.pack(pady=10)
score_label.pack(pady=20)

# for run theapplication
root.mainloop()
