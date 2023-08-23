# Funkcje w jezyku Python.

# przyklad funkcji zwracajacej wynik
def average(list):
    average = 0.0

    for l in list:
        average += l
    
    return average / len(list)

# przyklad funkcji anonimowej (lambda)
# cialem musi byc pojedyncze wyrazenie, nie moze zawierac print czy return
average_lambda = lambda list: sum(list) / len(list)

# przyklad funkcji nie zwracajacej wyniku
def print_triangle(h = 5):
    for y in range(h + 1):
        for x in range(y):
            print("o", end="")
        print()

# wywolania funkcji
print(average([1, 2]))
print(average_lambda([1, 2, 3]))
print_triangle(8)
