class Noeud:
    # attribut de classe
    arbre_vide = None

    """Constructeur d'un noeud d'un arbre binaire"""

    def __init__(self, v, g, d):
        self._valeur = v
        self._gauche = g
        self._droit = d

    # selecteurs
    def valeur(self):
        return self._valeur

    def gauche(self):
        return self._gauche

    def droit(self):
        return self._droit

    # methode de classe
    def est_vide(arbre):
        return arbre is Noeud.arbre_vide

    def est_feuille(arbre):
        if arbre.gauche() == Noeud.arbre_vide and arbre.droit() == Noeud.arbre_vide:
            return True
        return False


def taille(self: Noeud):
    if self == Noeud.arbre_vide:
        return 0
    return 1 + taille(self.gauche()) + taille(self.droit())


def compte_feuilles(arbre: Noeud):
    if arbre == Noeud.arbre_vide:
        return 0
    if arbre.est_feuille():
        return 1
    return compte_feuilles(arbre.gauche()) + compte_feuilles(arbre.droit())

def hauteur(arbre: Noeud):
    if arbre == Noeud.arbre_vide:
        return 0
    if arbre.droit() == None:
        return hauteur(arbre.gauche()) + 1
    if arbre.gauche() == None:
        return hauteur(arbre.droit()) + 1
    return hauteur(arbre.gauche()) + hauteur(arbre.droit()) + 1


A_g = Noeud("D", None, None)
A_N = None
A_1 = Noeud("A", Noeud("B", None, None), None)
A_2 = Noeud("A", Noeud("B", None, None), Noeud("D", None, None))
A_3 = Noeud("A", Noeud("B", None, Noeud("C", None, None)),
            Noeud("D", None, None))
A_4 = Noeud("A", Noeud("B", Noeud("E", None, None),
            Noeud("C", None, None)), Noeud("D", None, None))

print(A_3.gauche().droit().valeur())
print(A_3.est_feuille())
print(compte_feuilles(A_N))
print(compte_feuilles(A_g))
print(compte_feuilles(A_3))
print(compte_feuilles(A_4))
print(taille(A_N))
print(hauteur(A_N))
print(hauteur(A_4))