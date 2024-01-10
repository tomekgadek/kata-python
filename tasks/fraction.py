"""
    Klasa Fraction potrafi wykonac podstawowe operacje na ulamkach zwyklych.
"""

def euklides(m, n):
    """ Metoda pomocnicza, ktory wyznacza najwiekszy wspolny dzielnik """
    if m % n == 0:
        return n
    else:
        return euklides(n, m % n)

class Fraction:
    def __init__(self, numerator, denominator = 1):
        nwd = euklides(numerator, denominator)
        self.numerator = numerator / nwd
        self.denominator = denominator / nwd

    def __str__(self):
        return "%d/%d" % (self.numerator, self.denominator)
    
    def __mul__(self, other):
        if type(other) == type(5):
            other = Fraction(other)
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)
    
    __rmul__ = __mul__

    def __add__(self, other):
        if type(other) == type(5):
            other = Fraction(other)
        return Fraction(self.numerator * other.denominator + self.denominator*other.numerator, 
                        self.denominator * other.denominator)
    
    __radd__ = __add__

    def __cmp__(self, other):
        diff = (self.numerator * other.denominator - self.denominator * other.numerator)
        return diff
    
    def __sub__(self, other):
        if type(other) == type(5):
            other = Fraction(other)
        return Fraction(self.numerator * other.denominator - self.denominator * other.numerator, 
                        self.denominator * other.denominator)
    
    def __rsub__(self, other):
        return Fraction(self.denominator * other - self.numerator, self.denominator)
    
    def __truediv__(self, other):
        if type(other) == type(5):
            other = Fraction(other)
        return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)
    
    def __rtruediv__(self, other):
        return Fraction(other * self.denominator, self.numerator)

    def __pos__(self):
        return Fraction(self.numerator, self.denominator)
    
    def __neg__(self):
        return Fraction(-self.numerator, self.denominator)
    
    def __invert__(self):
        return Fraction(self.denominator, self.numerator)
    
f1 = Fraction(2, 3)
f2 = Fraction(1, 2)
digit = 7

print("f1 = {}, f2 = {}, digit = {}".format(f1, f2, digit))
print("{} * {} = {}".format(f1, f2, f1 * f2))
print("{} * {} = {}".format(f1, digit, f1 * digit))
print("{} * {} = {}".format(digit, f1, digit * f1))
print("{} + {} = {}".format(f1, f2, f1 + f2))
print("{} + {} = {}".format(f1, digit, f1 + digit))
print("{} + {} = {}".format(digit, f2, digit + f2))
print("{} / {} = {}".format(f1, f2, f1/f2))
print("{} / {} = {}".format(f1, digit, f1/digit))
print("{} / {} = {}".format(digit, f2, digit/f2))
print("{} / {} = {}".format(f1, digit, f1/digit))
print("+{} = {}".format(f1, +f1))
print("-{} = {}".format(f1, -f1))
print("~{} = {}".format(f1, ~f1))
print("~{} = {}".format(f2, ~f2))
