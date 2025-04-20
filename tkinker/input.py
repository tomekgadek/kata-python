"""
    input.py: jak zastosować pole edycji w praktyce?
"""

import tkinter as tk
from tkinter import ttk

class QandAApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Q&A App")
        self.geometry("300x300")

        self.frame = ttk.Frame(self)
        self.frame.pack(pady=20, padx=20)

        self.label_question = ttk.Label(self.frame, text="24 * 5 = ?")
        self.label_question.grid(row=0, column=0, columnspan=2, pady=10)

        self.text_input = tk.Text(self.frame, height=3, width=30, bg="light yellow")
        self.text_input.grid(row=1, column=0, columnspan=2, pady=10)

        self.text_output = tk.Text(self.frame, height=3, width=30, bg="light cyan")
        self.text_output.grid(row=3, column=0, columnspan=2, pady=10)

        self.button_display = ttk.Button(self.frame, text="result", command=self.process_input)
        self.button_display.grid(row=2, column=0, columnspan=2, pady=10)

    def process_input(self):
        user_input = self.text_input.get("1.0", tk.END).strip()
        self.label_question.config(text=f"24 * 5 = {user_input}?")

        self.text_output.delete("1.0", tk.END)
        
        if user_input == "120":
            self.text_output.insert(tk.END, "Correct answer")
        else:
            self.text_output.insert(tk.END, "Wrong answer")


if __name__ == "__main__":
    app = QandAApp()
    app.mainloop()
