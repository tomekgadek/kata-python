"""
    rectangle.py: implementacja prostokata w przestrzeni 2D.
    
    TODO: klasa wymaga jeszcze refaktoryzacji.
"""

from point import Point
from vector import Vector

class RectangleError(Exception):
    """
        Wyjatek dla klasy Rectangle.
    """
    def __init__(self, message):
        self.message = message

class Rectangle:
    def __init__(self, x1 = 0, y1 = 0, x2 = 0, y2 = 0):
        if x1 == x2 or y1 == y2:
            raise RectangleError("Problem z konstrukcja prostokata.")
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
    def __str__(self):
        return f"R({self.pt1}, {self.pt2})"
    def __repr__( self ):
        return f"Rectangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y})"
    def center(self):
        a = Vector(self.pt1.x, self.pt2.x).length()
        b = Vector(self.pt1.y, self.pt2.y).length()

        return Point(self.pt1.x + a/2, self.pt1.y + b/2)
    def area(self):
        a = Vector(self.pt1.x, self.pt2.x).length()
        b = Vector(self.pt1.y, self.pt2.y).length()

        return a * b
    def move(self, x, y):
        self.pt1.x += x
        self.pt2.x += x
        self.pt1.y += y
        self.pt2.y += y

        return self
    def cover(self, other):
        """
            Zwraca prostokat, ktory pokrywa oba prostokaty.
        """
        x1 = min(self.pt1.x, other.pt1.x)
        y1 = min(self.pt1.y, other.pt1.y)
        x2 = max(self.pt2.x, other.pt2.x)
        y2 = max(self.pt2.y, other.pt2.y)

        return Rectangle(x1, y1, x2, y2)

if __name__ == "__main__":
    rectangle = Rectangle(0, 0, 6, 2)
    
    assert f"{rectangle}" == "R(P(0, 0), P(6, 2))"
    assert repr(rectangle) == "Rectangle(0, 0, 6, 2)"
    assert f"{rectangle.center()}" == "P(3.0, 1.0)"
    assert rectangle.area() == 12.0
    assert f"{rectangle.move(-1, 0)}" == "R(P(-1, 0), P(5, 2))"
    assert f"{rectangle.cover(Rectangle(1, 1, 2, 2))}" == "R(P(-1, 0), P(5, 2))"
