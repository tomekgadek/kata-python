# Rekurencja, cwiczenia praktyczne.

def print_stars(n):
    """Rekurencyjne wypisywanie n linii z gwiazdka."""
    if n > 0:
        print("*", end="")
        print_stars(n - 1)

def factorial(n):
    """Rekurencyjne obliczanie funkcji silnia n!"""
    if n == 0:
        return 1

    return n * factorial(n - 1)

def fibonacci(n):
    """Ciag Fibonacciego (definicja rekurencyjna)."""
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print("1. Rysowanie gwiazdek: ", end="")
print_stars(10)

print("")

print("2. Silnia: ", end="")
print(factorial(4))

print("3. Fibonacci: ", end="")
print(fibonacci(5))
