"""
    Skrypt potrafi przeksztalcic skomplikowana liste na liste plaska.

    Przyklad:

    [1, [2, 3], [[1]], (1, 2), [1, [1, 2]]] -> [1, 2, 3, 1, 1, 2, 1, 1, 2]
"""

def flatten(digits = []):

    if len(digits) == 0:
        return []
    
    if isinstance(digits[0], (list, tuple)):
        return flatten(list(digits[0]) + list(digits[1:]))
    else:
        return [digits[0]] + flatten(digits[1:])

assert flatten([[1], 2, [[3,4], 5], [[[]]], [[[6]]], 7, 8, [], (9, 10)]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
assert flatten([[1], []]) == [1]
assert flatten([[1, 2, (3, 4, [5, [6, [7]]])]]) == [1, 2, 3, 4, 5, 6, 7]
assert flatten([]) == []
assert flatten(()) == []
assert flatten((2, [3])) == [2, 3]
assert flatten(([1], 2, [3], (4, 5))) == [1, 2, 3, 4, 5]
assert flatten([1, [2, 3], [[1]], (1, 2), [1, [1, 2]]]) == [1, 2, 3, 1, 1, 2, 1, 1, 2]
