# Typy danych w jezyku Python.

# liczba calkowita type(age) = int
# liczba zmiennoprzecinkowa type(salary) = float
# liczba zespolona type(digit) = complex
# ciag tekstowy type(name) = string
# typ logiczny type(is_adult) = bool | True

age = 21    
salary = 2500.99   
digit = 4 + 3j
name = "John Doe"
is_adult = age >= 18

# typ lista type(languages) = list
# typ krotka type(digits) = tuple
# typ slownik type(translate) = dict
# typ zbior type(collection) = set

languages = ["Python", "Java", "Kotlin"]
digits = (1, 10, 100, 1000)
translates = {1: "one", 2: "two", 3: "three"}
collection = set([1, 6, 5, 2, 3, 4])

print("age is {}".format(type(age)))
print("languages is {}".format(type(languages)))
