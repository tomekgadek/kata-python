# Wyjatki w jezyku Python.

# przechwytywanie wyjatkow (podstawy)
try:
    # dzielenie przez 0 (wyjatek: ZeroDivisionError)
    1 / 0
except ZeroDivisionError:
    print("Wyjatek! Dzielenie przez 0!")
else:
    print("Wyjatek nie wystapil!")
finally:
    print("Tutaj zawsze sie wykona.")
print("Dalsze instrukcje")

# wyjatki jako klasy (przyklad), klasa dziedziczy po Exception
class MyError(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return "Wyjatek: " + str(self.message)

# zglaszanie wyjatku
raise MyError("Wystapil wyjatek...")
