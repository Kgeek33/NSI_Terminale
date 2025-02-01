def ecriture_binaire_entier_positif(n: int) -> str:
    binaire = ""
    while n >= 1:
        binaire = str(n % 2) + binaire
        n = n // 2
    return "0" if binaire == "" else binaire


assert ecriture_binaire_entier_positif(0) == "0"
assert ecriture_binaire_entier_positif(2) == "10"
assert ecriture_binaire_entier_positif(105) == "1101001"


def echange(tab, i, j):
    '''Echange les éléments d'indice i et j dans le tableau tab.'''
    temp = ...
    tab[i] = ...
    tab[j] = ...


def tri_bulles(tab):
    '''Trie le tableau tab dans l'ordre croissant
    par la méthode du tri à bulles.'''
    n = len(tab)
    for i in range(...):
        for j in range(...):
            if ... > ...:
                echange(tab, j, ...)
