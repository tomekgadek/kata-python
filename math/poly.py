"""
    poly.py: implementacja wielomianiu.
"""

from frac import *

class PolyError(Exception):
    """
        Wyjątek dla klasy Poly.
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

    def __sub__(self, other):
        """
            Odejmuje wielomian od innego wielomianu.
        """
        if isinstance(other, (int, float)):
            other = Poly(other)
        
        result = Poly(0, 1, max(self.size, other.size) - 1)
        
        for i in range(self.size):
            result.p[i] += self.p[i]
        
        for i in range(other.size):
            result.p[i] -= other.p[i]
        
        return result
    def __rsub__(self, other):
        """
            Odejmuje wielomian od liczby.
        """
        return Poly(other) - self
    def __mul__(self, other):
        """
            Mnoży wielomian przez inny wielomian.
        """
        if isinstance(other, (int, float)):
            other = Poly(other)
        
        result = Poly(0, 1, self.size + other.size - 2)
        
        for i in range(self.size):
            for j in range(other.size):
                result.p[i + j] = result.p[i + j] + (self.p[i] * other.p[j])
        
        return result
    __rmul__ = __mul__
    def __pos__(self):
        """
            Zwraca wielomian.
        """
        return self
    def __neg__(self):
        """
            Zwraca przeciwny wielomian.
        """
        result = Poly(0, 1, self.size - 1)
        
        for i in range(self.size):
            result.p[i] -= self.p[i]
        
        return result
    def eval(self, x):
        """
            Zwraca wartość wielomianu dla x.
        """
        result = self.p[-1]
        
        for i in range(self.size - 2, -1, -1):
            result = x * result + self.p[i]
        
        return result
    def combine(self, other):
        """
            Łączy dwa wielomiany.
        """
        result = Poly()
        
        for i in range(self.size):
            j = 0
            power = other
            while j < i - 1:
                power *= other
                j += 1
            result += Poly(self.p[i].x, self.p[i].y, 0) * power
        
        return result
    def __pow__(self, n):
        """
            Podnosi wielomian do potęgi n.
        """
        result = Poly(1)
        
        for i in range(n):
            result *= self
        
        return result
    def diff(self):
        """
            Zwraca pochodną wielomianu.
        """
        result = Poly(0, 1, self.size - 2)
        
        for i in range(1, self.size):
            result.p[i - 1] = i * self.p[i]
        
        return result
    def __getitem__(self, index):
        """
            Zwraca współczynnik wielomianu.
        """
        if index >= self.size:
            raise PolyError("Indeks poza zakresem!")
        return self.p[index]
    
    def __setitem__(self, index, value):
        """
            Ustawia współczynnik wielomianu.
        """
        if index >= self.size:
            raise PolyError("Indeks poza zakresem!")
        self.p[index] = value
    def is_zero(self):
        """
            Sprawdza, czy wielomian jest zerowy.
        """
        for data in self.p:
            if data != Frac(0):
                return False
        return True
    def __len__(self):
        """
            Zwraca długość wielomianu.
        """
        return self.size

if __name__ == "__main__":
    
    # Updated assertions and results
    fp1 = Poly(1, 2, 3)
    fp2 = Poly(1, 4, 2)

    # str
    assert f"{fp1}" == "[0, 0, 0, 1/2]"
    assert f"{fp2}" == "[0, 0, 1/4]"

    # add
    assert f"{1 + fp1 + fp2 + 2}" == "[3, 0, 1/4, 1/2]"

    # sub
    assert f"{-5 - (fp1 - fp2 + 2)}" == "[-7, 0, 1/4, -1/2]"

    # mul
    assert f"{2 * fp1 * fp2 * 2}" == "[0, 0, 0, 0, 0, 1/2]"

    # pos
    assert f"{+fp1}" == "[0, 0, 0, 1/2]"

    # neg
    assert f"{-fp1}" == "[0, 0, 0, -1/2]"

    # eval
    assert f"{fp2.eval(0.5)}" == "1/16"

    # combine
    assert f"{fp1.combine(fp2)}" == "[0, 0, 0, 0, 0, 0, 1/128]"

    # pow
    assert f"{fp2 ** 2}" == "[0, 0, 0, 0, 1/16]"

    # diff
    assert f"{fp1.diff()}" == "[0, 0, 3/2]"

    # is_zero
    assert fp1.is_zero() == False
    assert Poly().is_zero() == True

    # len
    assert len(fp2) == 3

    # get
    assert f"{fp1[3]}" == "1/2"
