# Standardowe wejscie / wyjscie w jezyku Python.

# metody odpowiedzialne za odczytanie napisow wprowadzonych na standardowe 
# wejscie

text = input("Podaj napis: ")
digit = int(input("Podaj cyfre: "))     # zastosowanie rzutowania

# niektore sposoby formatowania tekstu
print("Podano napis %s o liczbie znakow %d!" % (text, len(text)))
print("Wprowadzona cyfra to %d!" % digit)
