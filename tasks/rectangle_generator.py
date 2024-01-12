"""
    Generator czworokata.

    Output:
    +---+---+---+---+
    |   |   |   |   |
    +---+---+---+---+
    |   |   |   |   |
    +---+---+---+---+
"""

def rectangle_generator(width, height):

    first_line = "+" + ("---+" * width) + "\n"
    second_line = "|" + ("   |" * width) + "\n"

    rectangle = [first_line]

    for _ in range(height):
        rectangle.append(second_line)
        rectangle.append(first_line)
    
    return "".join(rectangle)

print(rectangle_generator(4, 2))
