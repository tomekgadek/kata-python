# Listy w jezyku Python.

l = []                      # tworzenie listy pustej
l = ["1", 1, 1.1]           # tworzenie listy, elementy nie musza byc tego 
                            # samego typu
l2 = list([1, 2])           # tworzenie listy z sekwencji

print(len(l))               # funkcja zwraca liczbe elementow listy
print(l + l2 + [0])         # listy mozna laczyc ze soba
print(3 * l)                # listy mozna powielac
print(l[2])                 # odwolanie do elementu listy za pomoca indeksu
print(l[0:2])               # odwolanie do elementow listy o indeksie 0 i 1 
                            # (wycinek)
l[1] = 1000                 # nadpisanie elementu listy znajdujacego sie pod 
                            # indeksem
                            # 1 wartoscia 1000
l[1:3] = [0]                # nadpisanie wycinka
l_copy = list(l)            # kopiowanie listy
l_copy = l[:]               # kopiowanie listy
print(2 in l)               # czy element znajduje sie na liscie (bool)
print(2 not in l)           # czy element nie znajduje sie na liscie (bool)

l2 = list(range(6))         # buduje liste od 0 do 5
l2 = list(range(2, 6))      # buduje liste od 2 do 5
l2 = list(range(1, 6, 2))   # buduje liste do 1 do 5 z krokiem iteracji = 2

del l2[1]                   # usuwanie elementu z listy o zadanym indeksie
del l[0:2]                  # usuwanie wycinka listy o zadanym zakresie
del l                       # usuwanie calej listy
