"""
    label.py: jak dodać etykietę do okna w tkinterze?
"""

from tkinter import Tk, Label

root = Tk()

root.title("Add label to window")
root.geometry("320x240")

# Użycie menedżera układu "pack" do umieszczenia etykiety na środku okna.
# Argumenty:
# - text: tekst wyświetlany na etykiecie.
# - font: rozmiar lub styl czcionki tekstu.
# - fg: kolor tekstu (kolor pierwszoplanowy) etykiety.
# - bg: kolor tła etykiety.
# - padx: wewnętrzne odstępy poziome w etykiecie.
# - pady: wewnętrzne odstępy pionowe w etykiecie.

label = Label(root, text="Look at me!", font=("Arial", 16), fg="#2E86C1", bg="#A9DFBF", padx=20, pady=20)
label.pack(expand=True)  # expand=True zapewnia wyśrodkowanie etykiety zarówno w poziomie, jak i w pionie.

root.mainloop()
