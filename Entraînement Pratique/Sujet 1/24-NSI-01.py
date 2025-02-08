def echange(tab, i, j):
    '''Échange les éléments d'indice i et j dans le tableau tab.'''
    temp = tab[i]
    tab[i] = tab[j]
    tab[j] = temp


def tri_selection(tab):
    '''Trie le tableau tab dans l'ordre croissant
    par la méthode du tri par sélection.'''
    N = len(tab)
    for k in range(N - 1):
        imin = k
        for i in range(k + 1, N):
            if tab[i] < tab[imin]:
                imin = i
        echange(tab, k, imin)


def taille(arbre, lettre):
    '''Renvoie la taille de l'arbre binaire.'''
    if lettre == '':
        return 0
    gauche = arbre[lettre][0]
    droite = arbre[lettre][1]
    return 1 + taille(arbre, gauche) + taille(arbre, droite)


tab = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
tri_selection(tab)
assert tab == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
