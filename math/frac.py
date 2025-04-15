"""
    frac.py: modul, ktory obsluguje podstawowe operacje na ulamkach.
"""

class FracError(Exception):
    def __init__(self, message):
        self.message = message

class Frac:
    def __init__(self, x = 0, y = 1):
        if y == 0:
            raise FracError("Dzielenie przez 0!")
        self.x = x // self._gcd(x, y)
        self.y = y // self._gcd(x, y)

    def __str__(self):
        return f"{self.x}/{self.y}" if self.y != 1 else str(self.x)

    def __repr__(self):
        return f"Frac(x={self.x}, y={self.y})"

    def __add__(self, other):
        other = self._recognize_type(other)
        
        denominator = self.y * other.y
        first_numerator = int(denominator / self.y) * self.x
        second_numerator = int(denominator / other.y) * other.x

        return Frac(first_numerator + second_numerator, denominator)
    
    __radd__ = __add__
    
    def __sub__(self, other):
        other = self._recognize_type(other)

        denominator = self.y * other.y
        first_numerator = int(denominator / self.y) * self.x
        second_numerator = int(denominator / other.y) * other.x

        return Frac(first_numerator - second_numerator, denominator)
    
    def __rsub__(self, other):
        other = self._recognize_type(other)
        
        return Frac(other.x * self.y - self.x * other.y, self.y * other.y)
    
    def __mul__(self, other):
        other = self._recognize_type(other)

        return Frac(self.x * other.x, self.y * other.y)

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = self._recognize_type(other)

        return Frac(self.x * other.y, self.y * other.x)

    def __rtruediv__(self, other):
        other = self._recognize_type(other)
        
        return Frac(self.y * other.x, self.x * other.y)

    def __pos__(self):
        return Frac(self.x, self.y)

    def __neg__( self ):
        return Frac(-self.x, self.y)

    def __invert__(self):
        return Frac(self.y, self.x)

    def _gcd(self, a, b):
        while b != 0:
            c = a % b
            a = b
            b = c
        return a
    
    def _float_to_frac(self, digit_as_float = None):
        float_txt = str(digit_as_float)
        l = float_txt[:float_txt.find(".")]
        m = float_txt[float_txt.find("." ) + 1:]

        numerator = int(l) * pow(10, len(m)) + int(m)
        denomintor = pow(10, len(m))

        return Frac(numerator, denomintor)
    
    def _recognize_type(self, other):
        if(isinstance(other, int)):
            return Frac(other)
        elif (isinstance(other, float)):
            return self._float_to_frac(other)

        return other
    
    def __eq__(self, other):
        if isinstance(other, int):
            return self.x == other * self.y
        elif isinstance(other, float):
            return self.x / self.y == other

        return self.x * other.y == other.x * self.y
    
    def __ne__(self, other):
        return not self.__eq__(other)

if __name__ == "__main__":
    f_1_4 = Frac(1, 4)
    f_1_2 = Frac(1, 2)
    
    assert f"{f_1_4}" == "1/4"
    assert repr(f_1_4) == "Frac(x=1, y=4)"
    assert str(f_1_4 + f_1_2) == "3/4"
    assert str(f_1_4 - f_1_2) == "-1/4"
    assert str(2 - f_1_2) == "3/2"
    assert str(f_1_2 - 2.0) == "-3/2"
    assert str(f_1_4 * f_1_2) == "1/8"
    assert str(f_1_4 / f_1_2) == "1/2"
    assert str(1 + f_1_2) == "3/2"
    assert str(2.0 * f_1_4) == "1/2"
    assert str(f_1_4 * 2.0) == "1/2"
    
    # operatory jednoargumentowe
    assert f"{+f_1_2}" == "1/2"
    assert f"{-f_1_2}" == "-1/2"
    assert f"{~f_1_2}" == "2"
