"""
    Wyznaczenie liczb pierwszych ze zbioru <2, n>. Sito Erastotenesa.

    Pseudokod działania algorytmu:

    Wejscie: Liczba calkowita n > 1.

    Tablica A powinna zawierac typy logiczne oraz powinna być indeksowana od 2 do n.
    Tablice A wypelniamy poczatkowo wartosciami 'True'.

    Dla (for) i = 2, 3, 4... do sqrt(n).
    Jezeli A[i] = True
        Dla (for) j = 2*i, 3*i, 4*i... do n
            A[j] = False

    Wyjscie: Wartosci 'i' takie, ze A[i] zawiera wartosc True.     
"""

import math

def find_prime_numbers(n):
    I = [True for _ in range(0, n+1)]

    i = 2
    while i <= math.sqrt(n):

        if I[i] == True:
            x = 2
            j = x * i
            while j <= n:
                I[j] = False
                x += 1
                j = x * i
        i += 1

    O = []

    for index, item in enumerate(I):
        if item == True and index > 1:
            O.append(index)
    
    return O

n = 60
print(find_prime_numbers(n))