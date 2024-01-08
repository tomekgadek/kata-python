"""
    Implementacja kolejki w oparciu o liste.

    Jezeli czekasz na swoja kolej w sklepie miesnym to sie nie martw - to jest kolejka FiFo.
"""

class Queue:
    def __init__(self):
        self.items = []
    
    def __str__(self):
        return str(self.items)
    
    def put(self, item):
        self.items.append(item)
    
    def get(self):
        if len(self.items) == 0:
            return None
        return self.items.pop(0)

queue = Queue()

queue.put(1)
queue.put(2)
queue.put(3)
assert str(queue) == "[1, 2, 3]"

queue.put(4)
assert str(queue) == "[1, 2, 3, 4]"

queue.get()
assert str(queue) == "[2, 3, 4]"

queue.get()
assert str(queue) == "[3, 4]"
