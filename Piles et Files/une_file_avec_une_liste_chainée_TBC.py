from  classe_maillon import *

class File:
    """structure de file"""
    def __init__(self):
        self.tete = None
        self.queue = None

    def est_vide(self):
        return self.tete is None

    def retirer(self):
        """ retire le maillon de tête """
        pass
    def ajouter(self, x):
        """ajoute un maillon en queue de la file"""
        pass

    #permet l'appel str(L1) equivalent Ã  L1.__str__()
    def __str__(self, chaine="["):
        return str(self.tete)

    def __len__(self):
        return taille_iter(self.tete)


F= File()
print("file vide ?", F.est_vide())
F.ajouter(5)
print(str(F))
F.ajouter(8)
print(str(F))
F.ajouter(-2)
print(str(F))
#n =premier(F)
n=F.retirer()
print("premier retirÃ© =",n)
print("file vide ?", F.est_vide())
print(str(F))


