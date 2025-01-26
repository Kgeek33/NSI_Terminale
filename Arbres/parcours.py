from classe_noeud import Noeud, hauteur, compte_feuilles, taille


def parcours_infixe(self: Noeud):
    if self == Noeud.arbre_vide:
        return ""
    return (
        parcours_infixe(self.gauche()) +
        str(self.valeur()) + " " +
        parcours_infixe(self.droit())
    )


def parcours_prefixe(self: Noeud):
    if self == Noeud.arbre_vide:
        return ""
    return (
        str(self.valeur()) + " " +
        parcours_prefixe(self.gauche()) +
        parcours_prefixe(self.droit())
    )


def parcours_posfixe(self: Noeud):
    if self == Noeud.arbre_vide:
        return ""
    return (
        parcours_posfixe(self.gauche()) +
        parcours_posfixe(self.droit()) +
        str(self.valeur()) + " "
    )


def parcours_en_largeur(a):
    if a is None:
        return
    h = hauteur(a)
    print("hauteur =", h)
    for i in range(0, h+1):
        # i = 0 -> niveau de la racine --- i=h -> niveau des feuilles
        parcourir_niveau(a, i)
    print()


def parcourir_niveau(a, n):
    if a is None:
        return
    if n == 0:
        # on est descendu de n niveaux depuis la racine de a : on affiche
        # la valeur du noeud
        print(a.valeur(), end=" ")
    elif n > 0:
        # on est au-dessus du niveau n à afficher : on descend sur l'arbre
        # gauche, puis sur l'arbre droit
        parcourir_niveau(a.gauche(), n-1)
        parcourir_niveau(a.droit(), n-1)


def table_infixe(a, tab=None):
    """ renvoie la liste des éléments de a lus dans un parcours infixe """
    if a is None:
        return []
    if tab is None:
        tab = []
    return parcours_infixe(a).split(" ")[:-1]


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

if __name__ == "__main__":
    print(A_3.gauche().droit().valeur())
    print(A_3.est_feuille())
    print(compte_feuilles(A_N))
    print(compte_feuilles(A_g))
    print(compte_feuilles(A_3))
    print(compte_feuilles(A_4))
    print(taille(A_N))
    print(hauteur(A_4))
    print(hauteur(A_2))
    print(hauteur(A_3))
    print(parcours_infixe(A_4))
    print(parcours_prefixe(A_4))
    print(parcours_posfixe(A_4))
    parcours_en_largeur(A_4)
    print(table_infixe(A_4))
