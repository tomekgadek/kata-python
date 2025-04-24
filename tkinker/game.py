"""
    game.py: implementacja prostej gry typu 'paper, rock, scissors' w Tkinterze
"""

import tkinter as tk
import random

from tkinter import Label, Button


class GameApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Paper | Rock | Scissors")
        self.geometry("500x250")

        self.available_choices = {
            "paper": "📃",
            "rock": "🪨",
            "scissors": "✂️"
        }

        self.label = Label(self, text="Zagrajmy w Papier, Kamień, Nożyce!", font=40)
        self.label.pack(pady=10)

        Button(self, text="📃 Papier", command=lambda: self.play_cmd("paper")).pack(pady=5)
        Button(self, text="🪨 Kamień", command=lambda: self.play_cmd("rock")).pack(pady=5)
        Button(self, text="✂️ Nożyce", command=lambda: self.play_cmd("scissors")).pack(pady=5)

    def play(self, player, cpu):
        win_with = {"paper": "rock", "rock": "scissors", "scissors": "paper"}
        if player == cpu:
            return None
        elif win_with[player] == cpu:
            return True
        else:
            return False

    def choice(self):
        return random.choice(list(self.available_choices.keys()))

    def play_cmd(self, player):
        cpu = self.choice()
        is_user_winner = self.play(player, cpu)

        player_choice = self.available_choices[player]
        cpu_choice = self.available_choices[cpu]

        if is_user_winner is None:
            self.label.config(
                text=f"Remis! GRACZ({player_choice}) vs CPU({cpu_choice}). Spróbuj ponownie!",
                foreground="blue"
            )
        elif is_user_winner:
            self.label.config(
                text=f"Wygrałeś! GRACZ({player_choice}) vs CPU({cpu_choice}). Zagrajmy jeszcze raz!",
                foreground="green"
            )
        else:
            self.label.config(
                text=f"Przegrałeś! GRACZ({player_choice}) vs CPU({cpu_choice}). Spróbuj ponownie!",
                foreground="red"
            )


if __name__ == "__main__":
    app = GameApp()
    app.mainloop()
