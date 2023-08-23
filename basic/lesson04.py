# Lancuchy znakow w jezyku Python.         

s = ''                      # tworzenie pustego ciagu tekstowego
s = ""                      # tworzenie pustego ciagu tekstowego
s = "python"                # tworzenie ciagu tekstowego
s = str([1, 2, 3])          # postac naspisowa obiektu

print(s)
print(len(s))               # dlugos napisu, liczba znakow w ciagu tekstowym

s = "Python"
print("Jezyk" + s)          # konkatenacja, laczenie ciagow tekstowych
print(2 * s)                # powielanie ciagu tekstowego
print(s[3])                 # odniesienie sie do konkretnego znaku

print(s[:3])                # wyciecie 3 pierwszych znakow
print(s[2:5])               # wyciecie znakow o indeksie 2, 3 i 4

s_copy = s[:]               # kopiowanie ciagow tekstowych
s_copy = str(s)             # kopiowanie ciagow tekstowych

print(s_copy in s)          # zawieranie, zwraca typ logiczny (True, False)
print(s_copy not in s)      # zawieranie, zwraca typ logiczny (True, False)

print("%s 3.10" % s)        # formatowanie lancucha znakowego
print("%s == %s" % (2, 2))  # formatowanie lancucha znakowego
print("1. {}".format(s))    # formatowanie lancucha znakowego

del s                       # usuwanie lancucha znakowego
