from classe_maillon import Maillon, taille_iter


class File:
    """structure de file"""

    def __init__(self):
        self.tete = None
        self.queue = None

    def est_vide(self):
        return self.tete is None

    def retirer(self):
        if self.est_vide():
            raise IndexError("retirer sur une file vide")
        v = self.tete.valeur()
        # disparition du maillon de tete
        self.tete = self.tete.suite()
        # si la file est vide, il n'y a plus de queue
        if self.tete is None:
            self.queue = None
        return v

    def ajouter(self, x):
        """ajoute un maillon en queue de la file"""
        # creation du maillon de queue
        m = Maillon(x, None)
        if self.est_vide():
            self.tete = m
        else:
            # un peu moche !....
            self.queue._suivant = m
        self.queue = m

    def vider(self):
        self.tete = None
        self.queue = None

    # permet l'appel str(L1) equivalent Ã  L1.__str__()
    def __str__(self, chaine="["):
        return str(self.tete)

    def __len__(self):
        return taille_iter(self.tete)


if __name__ == '__main__':

    F = File()
    print("file vide ?", F.est_vide())
    F.ajouter(5)
    print(str(F))
    F.ajouter(8)
    print(str(F))
    F.ajouter(-2)
    print(str(F))
    # n =premier(F)
    n = F.retirer()
    print("premier retiré =", n)
    print("file vide ?", F.est_vide())
    print(str(F))
