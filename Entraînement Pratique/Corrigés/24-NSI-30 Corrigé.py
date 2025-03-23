# exo 1
def fusion(tab1, tab2):
    '''Fusionne deux tableaux triés et renvoie le nouveau tableau trié.'''
    n1 = len(tab1)
    n2 = len(tab2)
    tab12 = [0] * (n1 + n2)
    i1 = 0
    i2 = 0
    i = 0
    while i1 < n1 and i2 < n2:
        if tab1[i1] < tab2[i2]:
            tab12[i] = tab1[i1]
            i1 = i1+1
        else:
            tab12[i] = tab2[i2]
            i2 = i2+1
        i += 1
    while i1 < n1:
        tab12[i] = tab1[i1]
        i1 = i1 + 1
        i = i+1
    while i2 < n2:
        tab12[i] = tab2[i2]
        i2 = i2 + 1
        i = i+1
    return tab12


assert fusion([3, 5], [2, 5]) == [2, 3, 5, 5]
assert fusion([-2, 4], [-3, 5, 10]) == [-3, -2, 4, 5, 10]
assert fusion([4], [2, 6]) == [2, 4, 6]
assert fusion([], []) == []
assert fusion([1, 2, 3], []) == [1, 2, 3]
# exo 2
romains = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def traduire_romain(nombre):
    """ Renvoie l'écriture décimale du nombre donné en chiffres
    romains """
    if len(nombre) == 1:
        return romains[nombre[0]]
    elif romains[nombre[0]] >= romains[nombre[1]]:
        return romains[nombre[0]] + traduire_romain(nombre[1:])
    else:
        return traduire_romain(nombre[1:])-romains[nombre[0]]


assert traduire_romain("XIV") == 14
assert traduire_romain("CXLII") == 142
assert traduire_romain("MMXXIV") == 2024
