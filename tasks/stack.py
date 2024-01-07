"""
    Implemetacja stosu w jezyku Python w oparciu o liste.

    Stos przypomina nalesniki ulozone na talerzu. Aby dobrac sie do konkretnego nalesnika musimy
    pobierac je kolejno rozpoczynajac od samej gory.
"""

class Stack:
    def __init__(self):
        self.items = []
    
    def __str__(self):
        return str(self.items)
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if len(self.items) == 0:
            return None
        return self.items.pop()
    
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
assert str(stack) == "[1, 2, 3]"

stack.pop()
assert str(stack) == "[1, 2]"

stack.push(4)
assert str(stack) == "[1, 2, 4]"

stack.pop()
stack.pop()
stack.pop()
assert str(stack) == "[]"

stack.pop()
assert str(stack) == "[]"
