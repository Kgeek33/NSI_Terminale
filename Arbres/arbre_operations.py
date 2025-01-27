from classe_noeud import Noeud


def est_feuille(A):
    return Noeud.est_vide(A.droit()) and Noeud.est_vide(A.gauche())


def compte_feuille(arbre):
    if arbre is None:
        return 0
    print(arbre.valeur())
    if est_feuille(arbre):
        return 1
    return compte_feuille(arbre.gauche())+compte_feuille(arbre.droit())


def taille(arbre):
    if Noeud.est_vide(arbre):
        return 0
    return 1 + taille(arbre.gauche()) + taille(arbre.droit())

# vers le parcours de l'arbre


def taille_bis(arbre):
    if Noeud.est_vide(arbre):
        return 0
    t_g = taille_bis(arbre.gauche())
    print("taille -- noeud de valeur {}".format(arbre.valeur()))
    t_d = taille_bis(arbre.droit())
    return 1 + t_g+t_d


def hauteur(arbre):
    assert not Noeud.est_vide(arbre)
    if est_feuille(arbre):
        return 0
    h1 = 0
    h2 = 0
    if not Noeud.est_vide(arbre.gauche()):
        h1 = 1 + hauteur(arbre.gauche())
    if not Noeud.est_vide(arbre.droit()):
        h2 = 1 + hauteur(arbre.droit())
    return max(h1, h2)


if __name__ == '__main__':
    # création avec la valeur  et deux sous-arbres
    A1 = Noeud('r', Noeud.arbre_vide, Noeud.arbre_vide)
    print(A1._valeur)  # 'r',
    print("A1 est vide ?", Noeud.est_vide(A1))  # False
    print("A1 gauche est vide ?", Noeud.est_vide(A1.gauche()))  # True

    a = Noeud('a', Noeud.arbre_vide, Noeud.arbre_vide)
    b = Noeud('b', Noeud.arbre_vide, Noeud.arbre_vide)
    A2 = Noeud('r', a, b)
    print(A2.gauche().valeur())     # 'a'
    print(Noeud.est_vide(A2))  # False

    A3 = (
        Noeud(3,
              Noeud(1,
                    Noeud(1, Noeud.arbre_vide, Noeud.arbre_vide),
                    Noeud.arbre_vide),
              Noeud(4,
                    Noeud(5, Noeud.arbre_vide, Noeud.arbre_vide),
                    Noeud(9, Noeud.arbre_vide, Noeud.arbre_vide)
                    ))
    )
    print("A3=", A3)

    print(A3.droit().gauche().valeur())  # 5
    print(Noeud.est_vide(A3.gauche().droit()))  # True

    print("nb de feuilles de A1, A2, A3 : {}, {}, {}".format(
        compte_feuille(A1), compte_feuille(A2), compte_feuille(A3)))
    print("taille de A1, A2, A3 : {}, {}, {}".format(
        taille(A1), taille(A2), taille(A3)))
    print("hauteur de A1, A2, A3 : {}, {}, {}".format(
        hauteur(A1), hauteur(A2), hauteur(A3)))

    A4 = Noeud(1,
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

    print("nb de feuilles de A4 : {}".format(compte_feuille(A4)))
    print("taille de A4 :{}".format(taille(A4)))
    print("hauteur de A4 : {}".format(hauteur(A4)))
