from random import shuffle
from classe_noeud import Noeud
from parcours import parcours_infixe, table_infixe


def ajouter(x: int, a: Noeud) -> Noeud:
    if a is None:
        return Noeud(x, None, None)
    if x < a.valeur():
        return Noeud(a.valeur(), ajouter(x, a.gauche()), a.droit())
    return Noeud(a.valeur(), a.gauche(), ajouter(x, a.droit()))


def construire(valeurs: list) -> Noeud:
    """renvoie l"ABR constitué des valeurs prises successivement
    dans la liste valeurs.
    valeurs[0] est la racine"""
    UNarbre = Noeud(valeurs[0], None, None)

    for blabla in valeurs:
        UNarbre = ajouter(blabla, UNarbre)

    return UNarbre


def appartient(x: any, a: Noeud) -> bool:
    if a is None:
        return False
    if x == a.valeur():
        return True
    if x < a.valeur():
        return appartient(x, a.gauche())
    return appartient(x, a.droit())


def premier(abr: Noeud):
    if abr.est_feuille() or abr.gauche() is None:
        return abr.valeur()
    return premier(abr.gauche())


def ordre_alphabetique(abr):
    if abr == Noeud.arbre_vide:
        return []
    return (
        ordre_alphabetique(abr.gauche()) +
        [abr.valeur()] +
        ordre_alphabetique(abr.droit())
    )


def trier_par_ABR(tab: list):
    abr = construire(tab)
    table_infixe(abr)


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
    print(appartient(4, arbreL0))
    print(appartient(19, arbreL))
    print(appartient(2, arbreLR))
    L_animaux = ["chat", "chien", "souris",
                 "araignée", "grenouille", "lézard", "zèbre"]
    A_animaux = construire(L_animaux)
    print(appartient("zèbre", A_animaux))
    print(appartient("éléphant", A_animaux))
    print(premier(A_animaux))
    print(ordre_alphabetique(A_animaux))
