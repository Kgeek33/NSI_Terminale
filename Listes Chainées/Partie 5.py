from classe_maillon import *


class Liste:
    """ une liste chaînée """

    def __init__(self) -> None:
        self.tete = None

    def est_vide(self) -> bool:
        return self.tete is None

    def ajoute(self, x) -> None:
        self.tete = Maillon(x, self.tete)

    def tete(self):
        return self.tete.valeur()

    def queue(self):
        return self.tete.suite()

    #permet l'appel str(L1) equivalent à L1.__str__()
    def __str__(self) -> str:
        # fait appel à la méthode __str__() de la classe Maillon
        return str(self.tete)


L1 = Liste()
L1.ajoute(10)  # [10]
L1.ajoute(20)  # [10, 20]
L1.ajoute(30)  # [10, 20, 30]
print(str(L1))
