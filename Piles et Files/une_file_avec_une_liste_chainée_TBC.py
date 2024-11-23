from classe_maillon import *


class File:
    """structure de file"""

    def __init__(self):
        self.tete: Maillon = None
        self.queue: Maillon = None

    def est_vide(self):
        return self.tete is None

    def retirer(self):
        """ retire le maillon de tête """
        if self.tete == None:
            raise ValueError("self.tete est vide !!")
        v = self.tete.valeur()
        self.tete = self.tete.suite()
        if self.tete is None:
            self.queue = None
        return v

    def ajouter(self, x):
        """ajoute un maillon en queue de la file"""
        m = Maillon(x, None)
        if self.tete != None:
            self.queue._suivant = m
        else:
            self.tete = m
        self.queue = m

    # permet l'appel str(L1) equivalent Ã  L1.__str__()
    def __str__(self, chaine="["):
        return str(self.tete)

    def __len__(self):
        return taille_iter(self.tete)

if __name__ == "__main__":
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
