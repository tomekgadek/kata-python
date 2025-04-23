"""
    game.py: implementacja prostej gry typu 'paper, rock, scissors' w Tkinterze
"""

# TODO: implementacja wymaga jeszcze refaktoryzacji.
# TODO: komunikaty są niejasne

import tkinter as tk
import random

from tkinter import Label, Button


class GameApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Paper, Rock, Scissors")
        self.geometry("300x150")

        self.available_choices = ["paper", "rock", "scissors"]

        self.label = Label(self, text="Let's play paper, rock, scissors!", font=40)
        self.label.pack(pady=10)

        Button(self, text="📃 Paper", command=lambda: self.play_cmd("paper")).pack(pady=5)
        Button(self, text="🤘 Rock", command=lambda: self.play_cmd("rock")).pack(pady=5)
        Button(self, text="✂️ Scissors", command=lambda: self.play_cmd("scissors")).pack(pady=5)

    def play(self, player, cpu):
        win_with = {"paper": "rock", "rock": "scissors", "scissors": "paper"}
        if player == cpu:
            return None
        elif win_with[player] == cpu:
            return True
        else:
            return False

    def choice(self):
        return random.choice(self.available_choices)

    def play_cmd(self, player):
        cpu = self.choice()
        is_user_winner = self.play(player, cpu)

        if is_user_winner is None:
            self.label.config(text="Tie! Try again!", foreground="blue")
        elif is_user_winner:
            self.label.config(text="You win... Let's play again", foreground="green")
        else:
            self.label.config(text="I win, I win!", foreground="red")


if __name__ == "__main__":
    app = GameApp()
    app.mainloop()
