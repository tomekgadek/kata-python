"""
    point.py: implementacja punktu w przestrzeni 2D.
"""

class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        """
            Zwraca reprezentację obiektu.
            Używane przez eval() do odtworzenia oryginalnego obiektu.
        """
        return f"Point(x={self.x}, y={self.y})"
    
    def __str__(self):
        """
            Zwraca reprezentację tekstową punktu.
        """
        return f"P({self.x}, {self.y})"
    
    def __eq__(self, value):
        if not isinstance(value, Point):
            return False
        return self.x == value.x and self.y == value.y

if __name__ == "__main__":
    point = Point(3, 4)
    
    assert f"{point}" == "P(3, 4)"
    assert repr(point) == "Point(x=3, y=4)"
