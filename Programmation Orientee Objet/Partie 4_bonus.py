from random import randint


class Personnage:
    # attributs de classe
    max_vies = id**2
    vies_utilisees = 0
    nb_personnages = 0

    def __init__(self, nom) -> None:
        self.vie = randint(0, Personnage.max_vies)
        self.nom = nom
        Personnage.nb_personnages += 1
        Personnage.vies_utilisees += self.vie
        if Personnage.vies_utilisees > 100:
            raise ValueError(f"mmlleddqugfywcgn ***** ->>>>>> {nom}")

    def __str__(self) -> str:
        return ("{} a {} points de vie".format(self.nom, self.vie))

    def le_plus_en_forme(p1, p2):
        if p1.vie > p2.vie:
            return p1
        return p2


kylian = Personnage("Kylian")
lucas = Personnage("Lucas")
florent = Personnage("Florent")
raphael = Personnage("le_chomeur_comme_m_sanchez")
