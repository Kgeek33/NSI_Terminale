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


def hauteur(self: Noeud):
    if self.est_feuille():
        return 0
    elif self.droit() == Noeud.arbre_vide:
        return 1 + hauteur(self.gauche())
    elif self.gauche() == Noeud.arbre_vide:
        return 1 + hauteur(self.droit())
    return 1 + max(hauteur(self.droit()), hauteur(self.gauche()))


def compte_feuilles(arbre: Noeud):
    if arbre == Noeud.arbre_vide:
        return 0
    if arbre.est_feuille():
        return 1
    return compte_feuilles(arbre.gauche()) + compte_feuilles(arbre.droit())
