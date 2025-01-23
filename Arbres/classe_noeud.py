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


def parcours_infixe(self: Noeud):
    """ affiche les valeurs de chaque noeud exploré séparées par des espaces """
    if self == Noeud.arbre_vide:
        return ""
    return parcours_infixe(self.gauche()) + str(self.valeur()) + ' ' + parcours_infixe(self.droit())


A_g = Noeud("D", None, None)
A_N = None
A_1 = Noeud("A", Noeud("B", None, None), None)
A_2 = Noeud("A", Noeud("B", None, None), Noeud("D", None, None))
A_3 = Noeud("A", Noeud("B", None, Noeud("C", None, None)),
            Noeud("D", None, None))
A_4 = Noeud(1,
            Noeud(2,
                  Noeud(4,
                        Noeud(8, Noeud.arbre_vide, Noeud.arbre_vide),
                        Noeud(9, Noeud.arbre_vide, Noeud.arbre_vide)),
                  Noeud(5,
                        Noeud(10, Noeud.arbre_vide, Noeud.arbre_vide),
                        Noeud.arbre_vide)),
            Noeud(3,
                  Noeud(6, Noeud.arbre_vide, Noeud.arbre_vide),
                  Noeud(7, Noeud.arbre_vide, Noeud.arbre_vide)))

# print(A_3.gauche().droit().valeur())
# print(A_3.est_feuille())
# print(compte_feuilles(A_N))
# print(compte_feuilles(A_g))
# print(compte_feuilles(A_3))
# print(compte_feuilles(A_4))
# print(taille(A_N))
# print(hauteur(A_4))
# print(hauteur(A_2))
# print(hauteur(A_3))
print(parcours_infixe(A_4))
