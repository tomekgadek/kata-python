# Wlasny modul w jezyku Python.

# zestawienie definicji kilku prostych funkcji
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

# sposob testowania modulu
# dzieki ponizszemu warunkowi uruchamiajac aktualny plik
# testy beda dostepne i widoczne, ale importujac ten oto
# plik testy zostana pominiete

if __name__ == "__main__":
    print("1 + 2 = ", add(1, 2))
    print("3 - 4 = ", sub(3, 4))
    print("3 * [2, 1] = ", mul(3, [2, 1]))
    print("7 / 3 = ", div(7, 3))
