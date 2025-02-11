from une_pile_avec_une_liste_chainée_TBC import Pile, inverser_pile


class File:
    """structure de file"""

    def __init__(self):
        self.pile_ar = Pile()
        self.pile_av = Pile()

    def est_vide(self):
        return self.pile_av.est_vide() and self.pile_ar.est_vide()

    def retirer(self):
        """ retire le maillon de tête """
        if self.est_vide():
            raise ValueError("Une des 2 piles est vide !!")

        if not self.pile_av.est_vide():
            v = self.pile_av.sommet()
            self.pile_av.depiler()
        else:
            while not self.pile_ar.est_vide():
                self.pile_av.empiler(self.pile_ar.depiler())
            v = self.pile_av.depiler()

        return v

    def ajouter(self, x):
        self.pile_ar.empiler(x)

    # permet l'appel str(L1) equivalent Ã  L1.__str__()
    def __str__(self, chaine="["):
        a = inverser_pile(self.pile_ar)
        return f"Pile avant : {str(self.pile_av)} et Pile arrière {str(a)}"

    def __len__(self):
        return self.pile_ar.taille()


F = File()
print("file vide ?", F.est_vide())
F.ajouter(5)
print(str(F))
F.ajouter(8)
print(str(F))
F.ajouter(-2)
print(str(F))
n = F.retirer()
print("premier retiré =", n)
print("file vide ?", F.est_vide())
print(str(F))
