# Krotki w jezyku Python.

t = ()              # utworzenie pustej krotki
t = (1,)            # utworzenie krotki z jedna skladowa
t = (1, 2, 3, 4, 5) # utworzenie krotki z 5 skladowymi
t = 1, 2, 3         # jezeli ilosc skladowych > 1 nawiasy nie sa obowiazkowe

t = (range(5))      # utworzenie krotki z sekwencji

print(t[4])         # dostep do skladowej krotki przy pomocy indeksu
print(t[1:3])       # wycinek elementow zawierajacych indeksy od 1 do 3 krotki
                    # macierzystej
print(len(t))       # rozmiar krotki
print((1,) + (7,))  # konkatenacja krotek
print(4 * (1, 2))   # powielanie krotek
print(100 in t)     # czy element znajduje sie w krotce (bool)
print(100 not in t) # czy element nie znajduje sie w krotce (bool)
a, b = 1, 2         # a = 0, b = 1, rozpakowanie krotki
a, b = b, a         # a = 1, b = 0, zamiana wartosci zmiennych
del t               # usuwanie krotki
