"""
    point.py: implementacja punktu w przestrzeni 2D.
"""

class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # reprezentacja obiektu
    # wywolanie eval() powinno odtworzyc oryginalny obiekt
    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"
    
    # reprezentacja tekstowa obiektu
    def __str__(self):
        return f"P({self.x}, {self.y})"

if __name__ == "__main__":
    point = Point(3, 4)
    
    assert f"{point}" == "P(3, 4)"
    assert repr(point) == "Point(x=3, y=4)"
