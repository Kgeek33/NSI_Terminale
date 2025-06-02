def fusion(tab1: list, tab2: list) -> list:
    min_tab1 = tab1[0]
    min_tab2 = tab2[0]
    tab_trié = []
    while len(tab1) != 0 and len(tab2) != 0:
        i = 0
        min_tab1 = tab1[i]
        min_tab2 = tab2[i]
        if min_tab1 < min_tab2:
            tab_trié.append(min_tab1)
        tab_trié.append(min_tab2)
        i += 1
    return tab_trié


assert fusion([3, 5], [2, 5]) == [2, 3, 5, 5]
assert fusion([-2, 4], [-3, 5, 10]) == [-3, -2, 4, 5, 10]
assert fusion([4], [2, 6]) == [2, 4, 6]
assert fusion([], []) == []
assert fusion([], [2, 5]) == [2, 5]
assert fusion([1, 2, 3], []) == [1, 2, 3]


romains = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500,"M":1000}


def traduire_romain(nombre):
    """ Renvoie l'écriture décimale du nombre donné en chiffres
    romains """
    if len(nombre) == 1:
        return romains[nombre[0]]
    elif romains[nombre[0]] >= romains[nombre[1]]:
        return romains[nombre[0]] + romains[nombre[1]]
    else:
        return traduire_romain(nombre[1: ])


assert traduire_romain("XIV") == 14
assert traduire_romain("CXLII") == 142
assert traduire_romain("MMXXIV") == 2024
