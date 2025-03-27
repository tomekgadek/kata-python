"""
    frac.py: modul, ktory obsluguje podstawowe operacje na ulamkach.
    
    TODO: jeszcze slabo to dziala:
    + ulamki powinny byc skracane
    + nie ma obslugi dzielenia przez 0
    + sporo technik bedzie do optymalizacji
"""

class Frac:
    def __init__(self, x = 0, y = 1):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}/{self.y}"

    def __repr__(self):
        return f"Frac(x={self.x}, y={self.y})"

    def __add__(self, other):
        denominator = self.y * other.y
        first_numerator = int(denominator / self.y) * self.x
        second_numerator = int(denominator / other.y) * other.x

        return Frac(first_numerator + second_numerator, denominator)
    
    def __sub__(self, other):
        denominator = self.y * other.y
        first_numerator = int(denominator / self.y) * self.x
        second_numerator = int(denominator / other.y) * other.x

        return Frac(first_numerator - second_numerator, denominator)

    def __mul__(self, other):
        return Frac(self.x * other.x, self.y * other.y)

    def __truediv__(self, other):
        return Frac(self.x * other.y, self.y * other.x)

    def __pos__(self):
        return Frac(self.x, self.y)

    def __neg__( self ):
        return Frac(-self.x, self.y)

    def __invert__(self):
        return Frac(self.y, self.x)

if __name__ == "__main__":
    f_1_4 = Frac(1, 4)
    f_1_2 = Frac(1, 2)
    
    assert f"{f_1_4}" == "1/4"
    assert repr(f_1_4) == "Frac(x=1, y=4)"
    assert str(f_1_4 + f_1_2) == "6/8"
    assert str(f_1_4 - f_1_2) == "-2/8"
    assert str(f_1_4 * f_1_2) == "1/8"
    assert str(f_1_4 / f_1_2) == "2/4"
    
    # operatory jednoargumentowe
    assert f"{+f_1_2}" == "1/2"
    assert f"{-f_1_2}" == "-1/2"
    assert f"{~f_1_2}" == "2/1"
