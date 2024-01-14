"""
    Program prezentuje roznice pomiedzy zwyklad rekurencja a rekurencja ogonowa.

    Funkcja sum() / sum_tail() sumuje liczby calkowite z zakresu <0, n>
"""

# zwykla rekurencja
def sum(n):
    if n == 0:
        return 0
    
    return n + sum(n-1)

# rekurecnja ogonowa
def sum_tail(n, acc=0):
    if n == 0:
        return acc
    
    acc += n
    return sum_tail(n-1, acc)

assert sum(3) == 6
assert sum(0) == 0
assert sum(4) == 10

assert sum_tail(3) == 6
assert sum_tail(0) == 0
assert sum_tail(4) == 10
