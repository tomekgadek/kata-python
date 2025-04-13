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
    
if __name__ == "__main__":
    
    fp1 = Poly(1, 2, 3)
    fp2 = Poly(1, 4, 2)

    assert f"{fp1}" == "[0, 0, 0, 1/2]"
    assert f"{fp2}" == "[0, 0, 1/4]"
