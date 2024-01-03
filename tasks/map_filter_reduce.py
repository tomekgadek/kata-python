"""
    Jak dzialaja funkcje map(), filter() i reduce()?
"""
from functools import reduce

items = [1, 2, 3, 4, 5]

squared_numbers = list(map(lambda digit: digit * digit, items)) # map() - transformacja danych
even_numbers = list(filter(lambda digit: digit % 2 == 0, items)) # filter() - filtrowanie danych
sum_numbers = reduce(lambda x, y: x + y, items) # reduce() - akumulacja danych

print("Squared numbers: ", squared_numbers)
print("Even numbers: ", even_numbers)
print("Sum numbers: ", sum_numbers)
