"""
    app_class.py: aplikacja tkinker zapakowana w klasę.
"""

import tkinter as tk

from tkinter import ttk
from tkinter.messagebox import showinfo


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # configure the root window
        self.title('My app')
        self.geometry('400x150')

        # tworze ramkę do organizacji widżetów
        self.frame = ttk.Frame(self)
        self.frame.pack(pady=20, padx=20)

        self.label = ttk.Label(self.frame, text='Hello, Tkinter!')
        self.label.grid(row=0, column=0, padx=10, pady=10)

        self.button = ttk.Button(self.frame, text='Click Me')
        self.button['command'] = self.click_button
        self.button.grid(row=0, column=1, padx=10, pady=10)

    def click_button(self):
        showinfo(title='Information', message='Hello, Tkinter!')

if __name__ == "__main__":
    app = App()
    app.mainloop()
