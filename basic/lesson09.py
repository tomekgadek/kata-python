# Instrukcja warunkowa.

# przyklad zastosowanie instrukcji warunkowej: if, elif, else

x = 17

if x % 2 == 0:
    print(x, "jest parzysta!")
else:
    print(x, "jest nieparzysta!")

if x > 0:
    print(x, "jest dodatnia!")
elif x < 0:
    print(x, "jest ujemna!")
else:
    print(x, "jest zerem!")

# przyklad zastosowanie wyrazenia trojargumentowego, A if B else C
# operatory logiczne: or (alternatywa), and (koniunkcja)

true_or_false = (True or False)
print("Wynik zapytania:")
print("Jednak prawda!" if true_or_false else "Jednak falsz!")
