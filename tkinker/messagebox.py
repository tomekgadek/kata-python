"""
    messagebox.py: jak dodać okno komunikatu w tkinterze?
"""

from tkinter import Tk, messagebox, Button

"""
    Wyświetla okno komunikatu z podanym tekstem.

    Argumenty:
    - param (str): Tekst, który zostanie wyświetlony w oknie komunikatu.
"""
def showMsg(param):
    messagebox.showinfo("Message window", param)

root = Tk()  
root.geometry("320x240")
root.title("Messagebox in tkinter")

"""
    Tworzy przycisk w oknie aplikacji.

    Argumenty:
    - root: okno główne, w którym przycisk zostanie umieszczony.
    - text (str): tekst wyświetlany na przycisku.
    - command (function): funkcja, która zostanie wywołana po kliknięciu przycisku.
"""
button = Button(root, text = 'Click me!', command = lambda:showMsg("Hello, World!"))
button.pack()
  
root.mainloop()
