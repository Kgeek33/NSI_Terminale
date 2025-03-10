from classe_maillon import Maillon, taille_rec, renverser


class Pile:
    """structure de pile"""

    def __init__(self):
        self.contenu = None
        self._taille = 0

    def est_vide(self):
        return self.contenu is None

    def empiler(self, v):
        self.contenu = Maillon(v, self.contenu)
        self._taille += 1

    def depiler(self):
        if self.est_vide():
            raise IndexError("impossible de depiler une pile vide !!!")
        v = self.contenu.valeur()
        self.contenu = self.contenu.suite()
        self._taille -= 1
        return v

    # permet l'appel str(L1) equivalent à L1.__str__()
    def __str__(self, chaine="["):
        return str(self.contenu)

    def sommet(self):
        if self.est_vide():
            raise IndexError("pas de sommet sur une pile vide !")
        return self.contenu.valeur()

    def vider(self):
        self.contenu = None
        self._taille = 0

    def taille(self):
        return taille_rec(self.contenu)


def inverser_pile(p):
    """prend en argument une pile p et inverse ses elements.
    Modifie la pile p"""
    n = p.taille()
    rev_p = Pile()
    for i in range(n):
        rev_p.empiler(p.depiler())
    # sans l'instruction suivante, la pile p est vide
    # à force de l'avoir dépilée !
    p.contenu = rev_p
    return rev_p


def pile_inverse(p):
    """prend en argument une pile p et qui renvoie une autre pile
    avec les éléments empilés dans l’ordre inverse.
    Ne modifie pas la pile p"""
    rev_pile = Pile()
    # utilise la fc renverser de la classe Maillon
    rev_pile.contenu = renverser(p.contenu)
    return rev_pile


if __name__ == '__main__':
    P = Pile()
    print("pile vide ?", P.est_vide())
    P.empiler(5)
    print(str(P))               # -> [5]
    P.empiler(8)
    print(str(P))               # -> [8, 5]
    P.empiler(-2)               # -> [-2, 8, 5]
    print(str(P))
    n = P.sommet()
    print("sommet =", n)  # -2
    # n=P.depiler()
    # print("sommet dépilé =",n)  # -2
    print("pile vide ?", P.est_vide())
    print("lg de la pile =", P.taille())
    print(str(P))
    # P.vider()
    print("lg de la pile =", P.taille())
    print("pile inversée:", str(pile_inverse(P)),
          "pile d'origine : ", str(P))  # p n'est pas modifiée !!
    print("inversion de pile:", str(inverser_pile(P)),
          "pile d'origine : ", str(P))  # p est inversée !!
