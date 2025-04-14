"""
    poly.py: implementacja wielomianiu.
"""

from frac import *

class PolyError(Exception):
    """
        Wyj�tek dla klasy FracPoly.
    """
    def __init__(self, message):
        self.message = message

class Poly:

    def __init__(self, x=0, y=1, n=0):
        """
            Tworzy wielomian c*x^n, gdzie c = x/y (wg Sedgewicka).
            x: licznik współczynnika
            y: mianownik współczynnika
            n: stopień wielomianu
        """
        if y == 0:
            raise PolyError("Dzielenie przez 0!")
        self.size = n + 1
        self.p = [Frac() for _ in range(self.size)]
        self.p[-1] = Frac(x, y)

    def __str__(self):
        """
            Zwraca stringa reprezentującego wielomian.
        """
        result = ", ".join([str(data) for data in self.p])
        return f"[{result}]"
    def __add__(self, other):
        """
            Dodaje wielomian do innego wielomianu.
        """
        if isinstance(other, (int, float)):
            other = Poly(other)
        
        max_size = max(self.size, other.size)
        result = Poly(0, 1, max_size - 1)
        
        for i in range(self.size):
            result.p[i] += self.p[i]
        
        for i in range(other.size):
            result.p[i] += other.p[i]
        
        return result
    __radd__ = __add__
    
if __name__ == "__main__":
    
    fp1 = Poly(1, 2, 3)
    fp2 = Poly(1, 4, 2)

    # str
    assert f"{fp1}" == "[0, 0, 0, 1/2]"
    assert f"{fp2}" == "[0, 0, 1/4]"

    # add
    assert f"{fp1 + fp2}" == "[0, 0, 1/4, 1/2]"
    assert f"{fp1 + 1}" == "[1, 0, 0, 1/2]"
    assert f"{2 + fp1}" == "[2, 0, 0, 1/2]"
    assert f"{1 + fp1 + 2 + fp2}" == "[3, 0, 1/4, 1/2]"
