"""
    vector.py: implementacja wktora.
"""

import math

class Vector:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"Vector(x={self.x}, y={self.y})"
    
    def __str__(self):
        return f"V({self.x}, {self.y})"
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, other):
        return self.x * other.x + self.y * other.y
    
    def length( self ):
        return math.sqrt(self.x ** 2 + self.y ** 2)

if __name__ == "__main__":
    v_4_3 = Vector(4, 3)
    v_1_1 = Vector(1, 1)
    v_2_2 = Vector(2, 2)
    v_5_1 = Vector(5, 1)
    vector = Vector(-2, 4)
    
    assert str(v_4_3) == "V(4, 3)"
    assert repr(vector) == "Vector(x=-2, y=4)"
    assert str(v_4_3 + v_2_2) == "V(6, 5)"
    assert str(vector - v_5_1) == "V(-7, 3)"
    assert (v_5_1 * v_1_1) == 6
    assert vector.length() == math.sqrt(20)
