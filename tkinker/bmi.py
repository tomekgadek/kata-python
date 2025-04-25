"""
    bmi.py: implementacja prostego kalkulatora BMI w Tkinterze
"""

from tkinter import *
from tkinter import messagebox

class BMICalculator(Tk):
    def __init__(self):
        super().__init__()
        self.title("*** BMI ***")
        self.geometry("400x267")
        self["background"] = 'dark orange'
        self.resizable(False, False)
        self.font = ("Helvetica", 20)

        self.create_widgets()

    def create_widgets(self):
        label_weight = Label(self, text="Twoja waga(kg):", background="dark orange", font=self.font)
        label_weight.place(x=40, y=40)

        self.text_weight = Text(self, height="1", width="10", highlightcolor="light yellow", font=self.font)
        self.text_weight.place(x=202, y=40)

        label_height = Label(self, text="Twój wzrost(cm):", background="dark orange", font=self.font)
        label_height.place(x=40, y=90)

        self.text_height = Text(self, height="1", width="10", highlightcolor="light yellow", font=self.font)
        self.text_height.place(x=202, y=90)

        self.label_result = Label(self, text="BMI wynosi: 00.0", background="dark orange", font=self.font)
        self.label_result.place(x=40, y=140)

        calculate_bmi_button = Button(self, text="Oblicz BMI", width="10", height="2", font=self.font, command=self.calculate_bmi)
        calculate_bmi_button.place(x=130, y=200)

    def calculate_bmi(self):
        weight_text = self.text_weight.get("1.0", END)
        height_text = self.text_height.get("1.0", END)

        try:
            weight = float(weight_text)
            height = float(height_text)

            height = height / 100.0

            bmi = (weight / (height ** 2))

            self.label_result["text"] = "BMI wynosi: {}".format(round(bmi, 1))
        except ValueError:
            messagebox.showerror('Message', 'Wprowadz prawidlowe dane do formularza!')

if __name__ == "__main__":
    app = BMICalculator()
    app.mainloop()