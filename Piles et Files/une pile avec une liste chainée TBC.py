from classe_maillon import *
from copy import deepcopy

class Pile:
    """structure de pile"""

    def __init__(self) -> None:
        # contenu est un maillon
        self.contenu = None
        self._taille = 0

    def est_vide(self) -> bool:
        return self.contenu is None

    def empiler(self, v: any) -> None:
        """ajoute un maillon dont la valeur est v en tête"""
        self.contenu = Maillon(v, self.contenu)
        self._taille += 1

    def depiler(self) -> any:
        if self.est_vide():
            raise IndexError("impossible de depiler une pile vide !!!")

        cqfs = self.contenu.valeur()
        self.contenu = self.contenu.suite()
        self._taille -= 1

        return cqfs

    # permet l'appel str(P) equivalent à P.__str__()
    def __str__(self, chaine="[") -> str:
        return str(self.contenu)

    def sommet(self) -> any:
        return self.contenu.valeur()

    def vider(self) -> None:
        self.contenu = None

    def taille(self) -> int:
        return self._taille

def inverser_pile(p: Pile) -> Pile:
    pcopy = deepcopy(p)
    nv = Pile()
    while not pcopy.est_vide():
        a = pcopy.depiler()
        nv.empiler(a)
    return nv


P = Pile()
print("pile vide ?", P.est_vide())
P.empiler(5)
print(str(P))
P.empiler(8)
print(str(P))
P.empiler(-2)
print(str(P))

print("L'oscar est desserné à .... -> ", P.sommet())
print("Voici la taille !!! -> ", P.taille())

P.vider()
print("pile vide ?", P.est_vide())

P.empiler(5)
P.empiler(-2)
n = P.depiler()
P.empiler(-2)

print("sommet dépilé =", n)
print("pile vide ?", P.est_vide())
print(str(P))
print(P.sommet())

print("Avant inversement -> ", P)
S = inverser_pile(P)
print("Après inversement -> ", P, S)
