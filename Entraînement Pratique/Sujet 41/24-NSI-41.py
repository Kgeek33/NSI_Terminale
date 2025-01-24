class Noeud:
    def __init__(self, etiquette, gauche, droit):
        self.v = etiquette
        self.gauche = gauche
        self.droit = droit


def taille(a: Noeud):
    if a == None:
        return 0

    return 1 + taille(a.gauche) + taille(a.droit)


def hauteur(a: Noeud):
    if a is None:
        return -1
    if a.gauche is None and a.droit is None:
        return 0
    elif a.droit is None:
        return 1 + hauteur(a.gauche)
    elif a.gauche is None:
        return 1 + hauteur(a.droit)
    return 1 + max(hauteur(a.droit), hauteur(a.gauche))


a = Noeud(1, Noeud(4, None, None), Noeud(0, None, Noeud(7, None, None)))

assert hauteur(a) == 2
assert taille(a) == 4
assert hauteur(None) == -1
assert taille(None) == 0
assert hauteur(Noeud(1, None, None)) == 0
assert taille(Noeud(1, None, None)) == 1


def ajoute(indice, element, tab):
    '''Renvoie un nouveau tableau obtenu en insérant
    element à l'indice indice dans le tableau tab.'''
    nbre_elts = len(tab)
    tab_ins = [0] * (nbre_elts + 1)
    for i in range(indice):
        tab_ins[i] = ...
    tab_ins[...] = ...
    for i in range(indice + 1, nbre_elts + 1):
        tab_ins[i] = ...
    return tab_ins
