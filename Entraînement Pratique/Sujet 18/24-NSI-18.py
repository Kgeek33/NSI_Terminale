def multiplication(n1, n2):
    if n1 == 0 or n2 == 0:
        return 0
    a = 0
    for _ in range(abs(n2)):
        a += n1

    if n1 < 0 and n2 < 0:
        return abs(a)
    return a


assert multiplication(3, 5) == 15
assert multiplication(-4, -8) == 32
assert multiplication(-2, 6) == -12
assert multiplication(-2, 0) == 0


def chercher(tab, x, i, j):
    '''Renvoie l'indice de x dans tab, si x est dans tab, 
    None sinon.
    On suppose que tab est trié dans l'ordre croissant.'''
    if i > j:
        return None
    m = (i + j) // 2
    if tab[m] < x:
        return chercher(tab, x, m, j)
    elif tab[m] > x:
        return chercher(tab, x, m, i)
    else:
        return m


assert chercher([1, 5, 6, 6, 9, 12], 7, 0, 10) == None
assert chercher([1, 5, 6, 6, 9, 12], 7, 0, 5) == None
assert chercher([1, 5, 6, 6, 9, 12], 9, 0, 5) == 4
assert chercher([1, 5, 6, 6, 9, 12], 6, 0, 5) == 2
