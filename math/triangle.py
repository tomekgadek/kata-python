"""
    triangle.py: implementacja prostokata w przestrzeni 2D.
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

if __name__ == "__main__":
    pass
