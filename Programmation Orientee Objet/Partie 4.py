class Personnage:
    # attributs de classe
    max_vies = 30
    nb_personnages = 0

    def __init__(self, nom, nbre_vies) -> None:
        self.vie = nbre_vies
        self.nom = nom
        Personnage.nb_personnages += 1  # accès à un attribut de classe

    def __str__(self) -> str:
        return ("{} a {} points de vie".format(self.nom, self.vie))

    def le_plus_en_forme(p1, p2):
        if p1.vie > p2.vie:
            return p1
        return p2


bob = Personnage("Bob", 15)
print(str(bob))
print("attributs de classe nb_personnages = {}, vu de Gandalf : {}".format(
    Personnage.nb_personnages, bob.nb_personnages))
gandalf = Personnage("Gandalf", 30)
print(str(gandalf))
print("attributs de classe max_vies = {}, vu de Gandalf : {}".format(
    Personnage.max_vies, gandalf.max_vies))
print("attributs de classe nb_personnages = {}, vu de Gandalf : {}".format(
    Personnage.nb_personnages, gandalf.nb_personnages))
le_plus_fort = Personnage.le_plus_en_forme(bob, gandalf)
print(f"{le_plus_fort.nom} a le plus de points de vies")
