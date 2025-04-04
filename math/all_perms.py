"""
    all_perms.py: generator wszystkich permutacji podanego zbioru.
"""

from itertools import permutations

digits = [2, 1, 0]

for perm in permutations(digits):
    print(perm)
