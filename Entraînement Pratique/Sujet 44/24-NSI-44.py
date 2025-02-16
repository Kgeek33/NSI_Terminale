def enumere(tab: list) -> dict[int, list[int]]:
    d: dict[int, list[int]] = {}
    for i in range(len(tab)):
        if tab[i] in d:
            d[tab[i]].append(i)
        else:
            d[tab[i]] = [i]
    return d


assert enumere([]) == {}
assert enumere([1, 2, 3]) == {1: [0], 2: [1], 3: [2]}
assert enumere([1, 1, 2, 3, 2, 1]) == {1: [0, 1, 5], 2: [2, 4], 3: [3]}


class Noeud:
    """Classe représentant un noeud d'un arbre binaire"""

    def __init__(self, etiquette, gauche, droit):
        """Crée un noeud de valeur etiquette avec
        gauche et droit comme fils."""
        self.etiquette = etiquette
        self.gauche = gauche
        self.droit = droit


def parcours(arbre, liste):
    """parcours récursivement l'arbre en ajoutant les étiquettes
    de ses noeuds à la liste passée en argument en ordre infixe."""
    if arbre is not None:
        parcours(arbre.gauche, liste)
        liste.append(arbre.etiquette)
        parcours(arbre.droit, liste)
    return liste


def insere(arbre: Noeud, cle):
    """insere la cle dans l'arbre binaire de recherche
    représenté par arbre.
    Retourne l'arbre modifié."""
    if arbre is None:
        return Noeud(cle, None, None)  # creation d'une feuille
    else:
        if arbre.gauche is not None:
            arbre.gauche = insere(arbre.gauche, cle)
        else:
            arbre.droit = insere(arbre.droit, cle)
        return arbre


arbre = Noeud(5, Noeud(2, None, Noeud(3, None, None)), Noeud(7, None, None))
assert parcours(arbre, []) == [2, 3, 5, 7]
for cle in (1, 4, 6, 8):
    arbre = insere(arbre, cle)
assert parcours(arbre, []) == [2, 3, 1, 4, 6, 8, 5, 7]
