# Slowniki w jezyku Python.

d = {}                  # utworzenie pustego slownika
d = {"I": 1, "V": 5}    # slownik o 2 elementach (klucz:wartosc)
print(len(d))           # liczba elementow klucz:wartosc
d["III"] = 3            # dodanie pozycji do slownika o nowym kluczu
print(d["V"])           # dostep do wartosci przy pomocy klucza
d_copy = dict(d)        # kopiowanie slownika
print("VI" in d_copy)   # czy klucz istnieje w slowniku
print("VI" not in d)    # czy klucz nie istnieje w slowniku
del d_copy["I"]         # usuwanie podanego klucza ze slownika
del d_copy              # usuwanie calego slownika
