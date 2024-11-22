from random import randint, shuffle
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

    def __str__(self, chaine="[") -> str:
        return str(self.contenu)

    def sommet(self):
        if self.est_vide():
            raise IndexError("pas de sommet sur une pile vide !")
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


def haut_bas_bas_haut(p):
    """ Échange le sommet et le fond de la pile p (p[-1] <-> p[0]) en temps O(n)."""
    # On dépile p pour remplir une pile p2
    haut = p.depiler()
    p_2 = Pile()
    while not p.est_vide():
        p_2.empiler(p.depiler())
    #le bas de p est maintenant le sommet de p_2. On le récupère et on le garde pour la fin
    bas = p_2.depiler()
    # on pose le haut au fond de p
    p.empiler(haut)
    # On rempile tout le reste dans p
    while not p_2.est_vide():
        p.empiler(p_2.depiler())  # Ordre inchangé pour ces valeurs là
    #on pose le bas tout en haut de p
    p.empiler(bas)

def melange(nb_cartes):
    """ melange deux paquets de nb_cartes chacun"""
    # On dépile p pour remplir une pile p2
    assert 0<=nb_cartes<100
    
    p_1 = Pile()
    p_2 = Pile()
    p_melange=Pile()
    L_1=[100+k for k in range(nb_cartes)]
    shuffle(L_1)
    L_2=[200+k for k in range(nb_cartes)]
    shuffle(L_2)
    # transforme les listes en piles
    for no_carte in range(nb_cartes):
        p_1.empiler(L_1[no_carte])
        p_2.empiler(L_2[no_carte])
    while not p_1.est_vide() and not p_2.est_vide():
        paquet_1=randint(0,1)
        if paquet_1==1:
            p_melange.empiler(p_1.depiler())
        else:
            p_melange.empiler(p_2.depiler())

    while not p_2.est_vide():
        p_melange.empiler(p_2.depiler())
    while not p_1.est_vide():
        p_melange.empiler(p_1.depiler())  
    return p_melange


if __name__ == '__main__':
    P = Pile()
    print("pile vide ?", P.est_vide())
    P.empiler(5)
    print(str(P))
    P.empiler(8)
    print(str(P))
    P.empiler(-2)
    print(str(P))
    P.empiler(15)
    P.empiler(16)
    P.empiler(17)
    haut_bas_bas_haut(P)

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
    print("Après inversement -> ", S)
    print("Nous allons mélanger 2 piles !")
    print(melange(P, S))
