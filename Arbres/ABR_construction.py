from random import shuffle
from classe_noeud import Noeud
from parcours import parcours_infixe


def ajouter(x: int, a: Noeud) -> Noeud:
    if a is None:
        return Noeud(x, None, None)
    if x < a.valeur():
        return Noeud(a.valeur(), ajouter(x, a.gauche()), a.droit())
    return Noeud(a.valeur(), a.gauche(), ajouter(x, a.droit()))


def construire(valeurs: list) -> Noeud:
    """renvoie l'ABR constitué des valeurs prises successivement
    dans la liste valeurs.
    valeurs[0] est la racine"""
    UNarbre = Noeud(valeurs[0], None, None)

    for blabla in valeurs:
        UNarbre = ajouter(blabla, UNarbre)

    return UNarbre


if __name__ == "__main__":
    L0 = [6, 8, 3, 1, 4, 9, 2, 7, 5]
    arbreL0 = construire(L0)
    print(parcours_infixe(arbreL0))
    L = [15, 10, 19, 17, 13, 16, 12, 8, 14]
    arbreL = construire(L)
    print(parcours_infixe(arbreL))
    shuffle(L)
    arbreLR = construire(L)
    print(parcours_infixe(arbreLR))
    L.sort()
    arbreLS = construire(L)
    print(parcours_infixe(arbreLS))
