def enumere(tab: list) -> dict:
    dico = {}
    if len(tab) == 0:
        return dico
    for i in range(len(tab)):
        if tab[i] in dico:
            dico[tab[i]].append(i)
        else:
            dico[tab[i]] = [i]
    return dico


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


def parcours(arbre: Noeud, liste: list) -> list:
    """parcours récursivement l'arbre en ajoutant les étiquettes
    de ses noeuds à la liste passée en argument en ordre infixe."""
    if arbre is not None:
        parcours(arbre.gauche, liste)
        liste.append(arbre.etiquette)
        parcours(arbre.droit, liste)
    return liste


def insere(arbre: Noeud, cle: int) -> Noeud:
    """insere la cle dans l'arbre binaire de recherche
    représenté par arbre.
    Retourne l'arbre modifié."""
    if arbre is None:
        return Noeud(cle, None, None)  # creation d'une feuille
    else:
        if cle < arbre.etiquette:
            arbre.gauche = insere(arbre.gauche, cle)
        else:
            arbre.droit = insere(arbre.droit, cle)
        return arbre


a = Noeud(5, None, None)
print(parcours(a, []))
insere(a, 2)
insere(a, 3)
insere(a, 7)
print(parcours(a, []))
