"""
    perms.py: modul, ktory obsluguje podstawowe operacje na permitacjach.
"""

"""
    p1 * p2

    Odpowiada zlozeniu funkcji: f * g(x) = f(g(x))
    
    f (perm1);
    g (perm2);
    i (x);
"""
def mul_perm(perm1, perm2):

    mul_perm = []
    for i in range(0, len(perm1)):
        mul_perm.append(perm1[perm2[i]])

    return mul_perm

"""
    p^-1
"""
def invert_perm(perm):
    
    inv_perm = perm.copy()
    
    for (i, value) in enumerate(perm):
        inv_perm[value] = i

    return inv_perm

"""
    is_identity(p)
    
    p[i] == i
"""
def is_identity(perm):
    
    for (i, value) in enumerate(perm):
        if value != i:
            return False
    return True


if __name__ == "__main__":

    N = 4

    p0 = range(N)
    p1 = [2, 1, 0]
    p2 = [1, 0, 2]
    p3 = [3, 0, 1, 2, 4]

    assert mul_perm(p1, p2) == [1, 2, 0]
    assert mul_perm(p2, p1) == [2, 0, 1]
    assert invert_perm(p3) == [1, 2, 3, 0, 4]
    assert is_identity(p0) == True
    assert is_identity(p2) == False
