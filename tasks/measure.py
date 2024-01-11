"""
    Generator miarki.

    Output:
    |....|....|....|....|....|....|....|....|....|....|....|....|....|
    0    1    2    3    4    5    6    7    8    9   10   11   12   13
"""

def generate_measure(border, scale, size):

    measure = []
    numbers = []
    
    measure.append(border)
    numbers.append("0")

    for counter in range(1, size + 1):
        measure.append(scale)
        measure.append(border)

        counter_as_str = str(counter)
        distance = " " * (len(scale) + 1 - len(counter_as_str))
        
        numbers.append(distance)
        numbers.append(counter_as_str)
    
    return "".join(measure) + "\n" + "".join(numbers)


print(generate_measure("|", "....", 13))
