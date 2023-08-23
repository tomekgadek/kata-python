# Petle programowe.

l = list(range(10, 90, 10))
s = set(range(1, 11))

# petla for (przyklad iteracji po indeksach)
for i, x in enumerate(l):
    print("lista[", i, "] = ", x)

# przyklad iteracji po elementach
for y in s:
    for x in s:
        print(x * y, "\t", end="")
    print()

# petla while (przyklad odwracania elementow w liscie)
i = 0
j = len(l) - 1

while i < j:
    l[i], l[j] = l[j], l[i]
    i += 1
    j -= 1
