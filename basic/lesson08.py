# Zbiory w jezyku Python.

s_a = set([0, 1, 2, 2, 4])      # utworzenie zbioru z sekwencji
s_b = set([3, 2, 1])

print(3 in s_a)                 # czy element nalezy do zbioru (bool)
print(3 not in s_a)             # czy element nie nalezy do zbioru (bool)

print(s_a <= s_b)               # czy zbior 'a' zawiera sie w zbior 'b' (bool)
print(s_a >= s_b)               # czy zbior 'b' zawiera sie w zbior 'a' (bool)
print(s_a | s_b)                # suma zbiorow
print(s_a & s_b)                # iloczyn zbiorow
print(s_a - s_b)                # roznica zbiorow
print(s_a ^ s_b)                # roznica symetryczna zbiorow
s_a = s_b.copy()                # kopiowanie zbiorow
