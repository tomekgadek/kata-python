"""
    simple_window_title_and_size.py: jak dodać tytuł i rozmiar okna w tkinterze?
"""

from tkinter import Tk

root = Tk()

root.title("My first window...")
root.geometry("400x150")

root.mainloop()