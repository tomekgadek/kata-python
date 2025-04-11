"""
    triangle.py: implementacja trojkota w przestrzeni 2D.
"""

from point import Point

class TriangleError(Exception):
    """
        Wyjatek dla klasy Rectangle.
    """
    def __init__(self, message):
        self.message = message

class Triangle:
    """
        Klasa reprezentująca trójkąt w przestrzeni 2D.
        Atrybuty:
            pt1 (Point): Pierwszy wierzchołek trójkąta.
            pt2 (Point): Drugi wierzchołek trójkąta.
            pt3 (Point): Trzeci wierzchołek trójkąta.
        Metody:
            __init__(x1, y1, x2, y2, x3, y3):
                Inicjalizuje trójkąt z trzema wierzchołkami. Zapewnia, że punkty
                tworzą poprawny trójkąt i nie są współliniowe ani nakładające się.
        Uwaga:
            Konstruktor zapewnia, że podane punkty nie nakładają się ani nie tworzą
            zdegenerowanego trójkąta (np. wszystkie punkty są współliniowe lub identyczne).
            Jest to osiągane poprzez weryfikację współrzędnych punktów przed utworzeniem trójkąta.
    """

    def __init__(self, x1 = 0, y1 = 0, x2 = 0, y2 = 0, x3 = 0, y3 = 0):
        points = {(x1, y1), (x2, y2), (x3, y3)}
        
        if len(points) < 3:
            raise TriangleError("Points must be distinct and non-collinear!")
        # Check for collinearity using the determinant method
        if x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2) == 0:
            raise TriangleError("Points must not be collinear!")
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        self.pt3 = Point(x3, y3)
    
    def __str__(self):
        return f"T({self.pt1}, {self.pt2}, {self.pt3})"
    
    def __repr__(self):
        return f"Triangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y}, {self.pt3.x}, {self.pt3.y})"
    
    def center(self):
        """
            Zwraca środek trójkąta.
        """
        x = (self.pt1.x + self.pt2.x + self.pt3.x) / 3.0
        y = (self.pt1.y + self.pt2.y + self.pt3.y) / 3.0
        return Point(x, y)    
    
    def area(self):
        """
            Zwraca pole powierzchni trójkąta.
        """

        # obliczam długości boków
        # wzór: # a^1/2 == aqrt(a)
        a = ((self.pt1.x - self.pt2.x) ** 2 + (self.pt1.y - self.pt2.y) ** 2) ** 0.5
        b = ((self.pt2.x - self.pt3.x) ** 2 + (self.pt2.y - self.pt3.y) ** 2) ** 0.5
        c = ((self.pt3.x - self.pt1.x) ** 2 + (self.pt3.y - self.pt1.y) ** 2) ** 0.5
        s = (a + b + c) / 2 # połowa obwodu
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5 # wzór Herona
    def move(self, x, y):
        """
            Przesuwa trójkąt o wektor (x, y).
        """
        for pt in (self.pt1, self.pt2, self.pt3):
            pt.x += x
            pt.y += y
        return self

if __name__ == "__main__":
    triangle = Triangle(0, 0, 4, 1, 2, 5)

    assert f"{triangle}" == "T(P(0, 0), P(4, 1), P(2, 5))"
    assert repr(triangle) == "Triangle(0, 0, 4, 1, 2, 5)"
    assert triangle.center() == Point(2.0, 2.0)
    assert round(triangle.area(), 2) == 9.00
    assert f"{triangle.move(-1, 0)}" == "T(P(-1, 0), P(3, 1), P(1, 5))"
