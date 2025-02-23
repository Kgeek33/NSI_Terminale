def nbr_occurrences(chaine: str) -> dict[str, int]:
    UNdic = {}
    chaineToList = list(chaine)
    for UNcarac in chaineToList:
        if UNcarac in UNdic:
            UNdic[UNcarac] += 1
        else:
            UNdic[UNcarac] = 1
    return UNdic


assert nbr_occurrences("Hello world !") == {
    'H': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 2, 'w': 1, 'r': 1, 'd': 1, '!': 1}


def fusion(tab1, tab2):
    '''Fusionne deux tableaux triés et renvoie
    le nouveau tableau trié.'''
    n1 = len(tab1)
    n2 = len(tab2)
    tab12 = [0] * (n1 + n2)
    i1 = 0
    i2 = 0
    i = 0
    while i1 < n1 and ...:
        if tab1[i1] < tab2[i2]:
            tab12[i] = ...
            i1 = ...
        else:
            tab12[i] = tab2[i2]
            i2 = ...
        i += 1
    while i1 < n1:
        tab12[i] = ...
        i1 = i1 + 1
        i = ...
    while i2 < n2:
        tab12[i] = ...
        i2 = i2 + 1
        i = ...
    return tab12
