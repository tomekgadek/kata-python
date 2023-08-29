"""
    Implementacja punktu w przestrzeni 2D i 3D.
"""

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return ("2D(%s, %s)" % (self.x, self.y))
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

class Point3D (Point2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z
    def __str__ (self):
        return ("3D(%s, %s, %s)" % (self.x, self.y, self.z))
    def __eq__(self, other):
        return super().__eq__(other) and self.z == other.z
    

p1 = Point2D(1, 2)
p2 = Point2D(1, 2)
p3 = Point2D(3, 4)

p4 = Point3D(1, 2, 3)
p5 = Point3D(1, 2, 3)
p6 = Point3D(3, 4, 3)

# __str__
print(p1)
print(p2)
print(p3)

print(p4)
print(p5)
print(p6)

# __eq__
print(p1 == p2)
print(p2 == p3)
print(p1 == p3)

print(p4 == p5)
print(p5 == p6)
print(p4 == p6)
