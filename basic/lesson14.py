# Klasy i dziedziczenie w jezyku Python.

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    def __str__(self):
        return "({}, {})".format(self.x, self.y)

class Rectangle:
    # podajemy lewy dolny i prawy gorny rog czworokata
    def __init__(self, x1 = 0, y1 = 0, x2 = 0, y2 = 0):
        # kompozycja w klasie Rectangle
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
    def __str__(self):
        return "Rectangle[{}, {}]".format(self.pt1, self.pt2)

class Square(Rectangle):
    # kwadrat to czworokat o rownych bokach
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        super().__init__(x1, y1, x2, y2)
        # sprawdzenie rownosci bokow
        if (x2 - x1) != (y2 - y1):
            raise Exception("it is not square")
    def __str__(self):
        return "Square[{}, {}]".format(self.pt1, self.pt2)

square = Square(0, 0, 6, 6)
print(square)
